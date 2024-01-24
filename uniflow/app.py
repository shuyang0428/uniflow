import sqlite3

from flask import Flask, jsonify, request
import threading
import uuid

from uniflow.flow.expand_reduce_flow import ExpandReduceFlow
from uniflow.node import Node
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp

app = Flask(__name__)

# In-memory storage for tracking jobs - for persistent storage, use a database
jobs = {}

@app.route('/expand-reduce-flow', methods=['POST'])
def expand_reduce_flow():
    data = request.json
    job_id = str(uuid.uuid4())
    jobs[job_id] = {'status': 'submitted', 'result': None}

    # Start the flow asynchronously in a new thread
    thread = threading.Thread(target=run_flow, args=(job_id, data))
    thread.start()

    return jsonify({'job_id': job_id}), 202

def run_flow(job_id, data):
    try:
        # Initialize and run the ExpandReduceFlow here with the provided data
        # For example, we need to create Node objects from the input data
        # and pass them to ExpandReduceFlow
        nodes = [Node(value_dict=d) for d in data]
        expand_op = ExpandOp(name="expand")
        reduce_op = ReduceOp(name="reduce")
        flow = ExpandReduceFlow(expand_op, reduce_op)

        # This is where we would actually run the flow and get the result
        result = flow.run(nodes)

        # Store the result in the job info
        jobs[job_id]['result'] = result
        jobs[job_id]['status'] = 'completed'
    except Exception as e:
        jobs[job_id]['status'] = 'error'
        jobs[job_id]['result'] = str(e)

@app.route('/jobs/<job_id>', methods=['GET'])
def get_job_status(job_id):
    job = jobs.get(job_id)
    if job is None:
        return jsonify({'message': 'Job not found'}), 404

    return jsonify({'job_id': job_id, 'status': job['status'], 'result': job['result']}), 200

DATABASE_PATH = 'uniflow.db'

@app.route('/expand-reduce-results', methods=['GET'])
def get_expand_reduce_results():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page

    # Connect to the database and retrieve the results
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT key, value FROM expand_reduce_output LIMIT ? OFFSET ?', (per_page, offset))
    results = cursor.fetchall()

    # Convert results to a list of dicts
    output = [dict(row) for row in results]

    return jsonify({
        'page': page,
        'per_page': per_page,
        'results': output
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
