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
  