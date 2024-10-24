# ASR system 
The automatic speech recognition system.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
python 3.9
poetry 1.5.1
```

### Installation
* Third party Package installation
```bash
cd code
python -m pip install --upgrade pip
pip install poetry==1.5.1
poetry install
```

## Run application
### Local
* Run API
```bash
uvicorn app.main:app --host 0.0.0.0 --port 80
```

### Docker 
* Build an image 
```bash
docker build -t whisper .
```
* Run  
```bash
docker run --rm -p 80:80 whisper
```

# Kube deployment
This application could be deployed on Kubernetes cluster. We're using the Minikube for local development.
Follow the steps below to deploy the application on Minikube.

Install Minikube
```bash
brew install minikube
```
First, start Minikube using the Docker driver. This will allow Minikube to use your local Docker daemon.
```bash
minikube start --driver=docker
```
To make Minikube use your local Docker images, you need to configure the Docker environment of Minikube. 
```bash
eval $(minikube -p minikube docker-env)
```
*Reverting to Host Docker Daemon*: If you want to switch back to using your host’s Docker daemon, simply run:
```bash
eval $(minikube -p minikube docker-env --unset)
```

To verify that you’re using the Minikube Docker daemon, run.
```bash
docker images
```

Build your Docker image locally using Docker.
```bash
docker build -t whisper .
```

Create a namespace called *whisper* where the application will be deployed.
```bash
kubectl create namespace whisper
```

Deploy the application.
```bash
kubectl apply -f kube
```

Run the following to get the local url to access the application:
```bash
minikube service whisper-service --url -n whisper
```


  