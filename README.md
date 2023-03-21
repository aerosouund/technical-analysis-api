# Thndr technical analysis API


![python](https://img.shields.io/badge/Python-3.8-3776AB.svg?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

A simple API for simulating a stock technical analysis, The app is divided into two microservices:
- The API Server
- A worker

The worker consumes data posted to a VerneMQ topic and persists them in a database, the API server handles requests for posting analysis and viewing
the stock prices. The analysis for a given stock is persisted on Redis for later retrieval from the stock endpoint


## To get started

- make sure helm is installed
- make sure your kubeconfig points to your local minikube cluster
- create the VerneMQ deployment & service
- run `deploy.sh` :fire:

### Technologies used

- MySQL
- Redis
- VerneMQ
- Flask
- SQLAlchemy


### Repo structure

- `apiserver`: The source code for the server
- `worker`: The source code for the worker
- `k8s`: The separate kubernetes manifests for the application
- `helm`: The entire application packaged as a helm chart
- `deploy.sh`: a script that creates the full infrastructure on a minikube cluster
