# Fibonacci Sequence API

## Overview
This API is a REST API that processes and return the Nth number in the Fibonacci sequence. This is built using Python and FastAPI.

## The Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It typically starts with 0 and 1. The sequence goes as follows:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Mathematically, it's defined as:
```
F(n) = F(n-1) + F(n-2)
Where:
F(0) = 0 and F(1) = 1
```

For example, to calculate the 5th Fibonacci number:
```
F(5) = F(4) + F(3) = 3 + 2 = 5
```

## Project Setup
1. Clone the repo
```
git clone https://github.com/your-username/FibonacciAPI.git
cd FibonacciAPI
```

2. Create the virtual Environment
```
python -m venv venv
source venv/scripts/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```
pip install -r requirements.txt
```

## Running the API
```
uvicorn app:app --reload
```
or
```python
python app.py
```
If everything is working properly the server should start at 
```
http://127.0.0.1:8000
```

# Testing the API

## Swagger
To access the Swagger UI go to
```
http://127.0.0.1:8000/docs
```
For the GET section make sure you input the number you want to calculate. For intance in the screen shot below we are using 10 in the paramaters field. To send the request press the 'Execute' button.

![Swagger UI Screenshot](./screenshots/swagger.png)

This will show the result of the API request as seen below. After sending the GET request with the number 10 we can see the Fibonacci response is 55 as shown below.

![Swagger UI Result Screenshot](./screenshots/Swagger_result.png)

## Curl
We can use curl to send a GET reauest to the API. To send a GET request you can try this:
```
curl -X GET "http://127.0.0.1:8000/fibonacci/10"
```

The response will look like this:
```
{"n":10,"fibonacci":55}
```

# Production Deployment

## Containerization
To ensure consistency across different environments and simplify deployment, this application can be containerized using Docker. Follow the steps below to build and run the Docker container for the Fibonacci API.
1. Create your 'dockerfile' in the root of your project directory. The dockerfile should contain the following content:

```Dockerfile
# Use the official Python image from the Docker Hub
FROM python:<version>

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Specify the command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

```
2. Build your docker image
To build the Docker image, run the following command in the terminal from the root of your project directory:
```
docker build -t fibonacci-api .
```
This command will build a Docker image named fibonacci-api using the instructions in the Dockerfile.
3. Run your Docker container
Once the image is built, you can run the container with the following command:
```
docker run -d -p 8080:8000 fibonacci-api
```
Your API is now running in a docker container and can be tested using the same methods as above:
## Swagger
To naviagte to the Swagger UI you can go here:
```
http://localhost:8000/docs
```
## Curl
To test the API using curl you can use the following commands:
```
curl -X GET "http://localhost:8000/fibonacci/10"
```

## Continuous Integration and Continuous Deployment (CI/CD) Pipeline Considerations
Implementing a CI/CD pipeline for this Fibonacci Sequence API ensures a smooth and efficient workflow for developing, testing, and deploying updates to the API. Here’s an overview of how CI/CD would benefit the project:
1. Automated Testing
2. Faster Delivery
3. Consistency Across Environments
4. Version Control and Rollbacks
5. Scalability

How would this API benefit from CI/CD?
1. Continuous Integration (CI):
A CI pipeline would allow automated tests and builds when new code is pushed to the repo. This ensures the app is stable.
2. Continuous Deployment (CD):
After the CI part of the pipeline has processed and succeded the CD part can take over. The CD pipeline can automate the deployment of the API to staging or production environments. This can be set up to trigger automatically or require manual approval, depending on the release strategy.

## Logging and Metrics
For logging and Metric collection we can use various tools like Prometheus and Grafana.

For scraping the Metrics from the API we can setup a '/Metrics' endpoint for Prometheus to scrape.
Then Grafana can be used to visualize the Prometheus data.

## scalability
- For deployments where scalability is needed we can use Kubernetes. Kubernetes will allow for Horizontal scaling. This will create multiple instances of your application and will load balance requests to each instance. This can be scaled up and down depending on the current influx of traffic.
- Caching can also be used to cache recently used numbers. This would allow for faster computation time for repeated requests.
- Load Balancing can be used to distribute traffic. Considering we are using K8s, the internal Load Balancer or an Ingress controller can distribute the traffic across all pods within your K8s.