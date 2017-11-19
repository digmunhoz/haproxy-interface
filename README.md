# How to execute

## Application Prereqs

* python
* python-dev
* pip
* virtualenv

## Running the API

First of all, you need to run the API which will read information from HAProxy using it socket file (HAProxy conf needs to have this: `stats  socket SOME_FILE`)

To execute the API, you need to follow these steps:

* Pull the project to a specific directory on HAProxy Server;
* Rename the file config_example.py to config.py (`src/api/config_example.py`);
* Inside the config file, change the parameter `haproxy_socket['DIR']` to point to the same place used on HAProxy config (`stats  socket` option);
* Start the virtualenv with the command  `source bin/activate`;
* Install the requirements running `pip install -r src/api/requirements.txt`;
* Enter on directory `src/api` and then run the command `uwsgi api.ini`.

>I'm gonna create an `install` and `init` script for all Linux distributions but I don't know when. For while, use the methods above to run the API.

## Running the Web Interface

* Pull the project to a specific directory on HAProxy Server;
* Rename the file config_example.py to config.py (`src/api/config_example.py`);
* Inside the config file, change the parameter `api_server['ADDRESS']` to point to the same network address from HAProxy Server (where the API is running);
* Still on config file, configure the parameter `ajax_api['ADDRESS']` to use the accessible IP where the API is running (this is the address which your browser will contact to get graphs information);
* Start the virtualenv with the command  `source bin/activate`;
* Install the requirements running `pip install -r src/web/requirements.txt`;
* Execute the command `python src/web/main.py`

## Development environment

I have created a very interesting way to run the whole environment on your computer using docker.

All of theses proccess is based on `make` command using the file `Makefile`.

The next, you'll see the instructions to manipulate the development environment.

### Prereqs

  - Docker and docker-compose installed on your computer (https://docs.docker.com/engine/installation/)

### Starting

The first command you'll have to run is `make build`.
This command will create the whole environment in your computer using docker. 

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

`http://localhost:5000`

### API

`http://localhost:5001/api/v1/info`

`http://localhost:5001/api/v1/errors`

`http://localhost:5001/api/v1/frontends`

`http://localhost:5001/api/v1/backends`

`http://localhost:5001/api/v1/servers`

## Screenshots

**Dashboard:**

![Dashboard](screenshots/HAProxyInterface-Dash.png)

**Servers and Backends:**

![](screenshots/HAProxyInterface-Servers.png)