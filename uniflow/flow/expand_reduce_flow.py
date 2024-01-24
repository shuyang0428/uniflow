from typing import Sequence

from uniflow.flow.db_utils import init_db, insert_flow_output
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.flow.flow import Flow
from uniflow.node import Node


class ExpandReduceFlow(Flow):
    def __init__(self, expand_op: ExpandOp, reduce_op: ReduceOp):
        """Initialize ExpandReduceFlow class.

        Args:
            expand_op (ExpandOp): An instance of ExpandOp.
            reduce_op (ReduceOp): An instance of ReduceOp.
        """
        super().__init__()
        self.expand_op = expand_op
        self.reduce_op = reduce_op

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run the expand and reduce operations.

        Args:
            nodes (Sequence[Node]): Nodes to process.

        Returns:
            Sequence[Node]: Nodes after processing.
        """
        # Assuming only one root node is passed
        root_node = nodes[0]

        # Perform expand operation
        expand_1, expand_2 = self.expand_op(root_node)

        # Perform reduce operation
        reduce_node = self.reduce_op(expand_1, expand_2)

        # After the flow operations, store the results in the database
        db_path = "uniflow.db"
        init_db(db_path)  # Ensure the database is initialized

        # Assuming the reduce_node contains the final key-value pairs as a dictionary in reduce_node.value_dict
        for key, value in reduce_node.value_dict.items():
            insert_flow_output(db_path, key, value)

        return [reduce_node]
