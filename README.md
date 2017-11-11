# How to execute

## Prereqs

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

## Some calls

### Web

`http://localhost:5000/home`

### API

`http://localhost:5000/api/info`

`http://localhost:5000/api/errors`
