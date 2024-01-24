# Backend Interview README
## Part 8: Documentation for Uniflow Application

### Setup and Installation Process

#### Installation Steps:

1. **Docker Dev Setup**:
   Build a Docker image using the Dockerfile, and
   Run the Docker container:
   ```bash
   docker build -t uniflow-app .
   docker run -p 5000:5000 uniflow-app

2. **k8s setup env**:
   Apply the Kubernetes configurations using kubectl:
   ```bash
    kubectl apply -f uniflow-deployment.yaml

## API Documentation

### Endpoints

#### Start ExpandReduceFlow Asynchronously

- **Endpoint**: `/expand-reduce-flow`
- **Method**: POST
- **Request Body** (JSON):
  ```json
  [
    {"key1": "value1", "key2": "value2"},
    {"key3": "value3"}
  ]
- **Response  Body** (JSON):
  ```json
  {
  "job_id": "unique-job-id"
  }
- **Example**:
  ```bash
  curl -X POST http://localhost:5000/expand-reduce-flow -d '[{"data1": "value1"}]' -H "Content-Type: application/json"

#### Check Job Status
- **Endpoint**: `/jobs/<job_id>`
- **Method**: GET
- **Response  Body** (JSON):
  ```json
  {
  "job_id": "unique-job-id",
  "status": "completed",
  "result": "result-data"
  }
- **Example**:
  ```bash
  curl http://localhost:5000/jobs/unique-job-id

#### Get ExpandReduceFlow Results
- **Endpoint**: `/expand-reduce-results`
- **Method**: GET
- **Query Parameters**: `page`, `per_page`
- **Response  Body** (JSON):
  ```json
  {
  "page": 1,
  "per_page": 10,
  "results": [
    {"key": "key1", "value": "value1"},
    {"key": "key2", "value": "value2"}
  ]
  }
- **Example**:
  ```bash
  curl "http://localhost:5000/expand-reduce-results?page=1&per_page=10"
