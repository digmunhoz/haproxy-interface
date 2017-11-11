# How to execute

## Application Prereqs

* python
* pip
* virtualenv

## Activate virtualenv

`source bin/activate`

## Install requirements

`pip install -r requirements.txt`

## Configure src/config.py

```
haproxy_socket = dict(                                                                                                                                        
    DIR = '/tmp',
    FILE = 'stats',
)
```

## Execute the app on the HAProxy server

`python src/main.py`

## Development environment

### Pre-reqs

  - Docker and docker-compose installed on your computer (https://docs.docker.com/engine/installation/)

### Starting

To start the environment, we'll use the `make` command as you can see below.

```
make build:	Create new development environment
make start:	Start development environment previously created
make stop:	Stop development environment
make status:	Show development environment
make restart:	Restart development environment
make logs:	Show development environment logs
make clean:	Clean dangling volume and images from docker
make help:	How to use make command
```

> **Note:**

> The first time you will need to run **make build**.

### Explaining Parameters

        - make build: When you want to create the environment executing again process such: migrate, deps install, requirements install, etc...;
        - make start: Just start the whole environment without change. This command does not execute the steps above;
        - make stop: As clear as water... To stop the environment;
        - make status: Another clear... Show environment status;
        - make restart: Do not need explanation;
        - make logs: Excellent way to see the logs of our containers;
        - make clean: Very important to clean you computer removing dangling volumes and images from docker;

### Accessing the environment

After the environment started, you can access by using the URL http://localhost:5000 on your browser.

## Some calls

### Web

`http://localhost:5000/home`

### API

`http://localhost:5000/api/info`

`http://localhost:5000/api/errors`
