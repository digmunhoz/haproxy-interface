# Importing modules
from flask import render_template
import socket
import requests

# Importing files
from base import app
import config

@app.route("/servers", methods=['GET'])
def servers():

    servers = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        config.api_endpoint['SERVERS']), timeout=config.connection_timeout
    ).json()

    backends = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        config.api_endpoint['BACKENDS']), timeout=config.connection_timeout
    ).json()

    servers_up = [s for s in servers if s['status'] == 'UP']
    servers_down = [s for s in servers if s['status'] != 'UP']
    
    backends_up = [b for b in backends if b['status'] == 'UP']
    backends_down = [b for b in backends if b['status'] != 'UP']

    servers_up = len(servers_up)
    servers_down = len(servers_down)
    backends_up = len(backends_up)
    backends_down = len(backends_down)

    return render_template('servers.html',
                            servers_up=servers_up,
                            servers_down=servers_down,
                            backends_up=backends_up,
                            backends_down=backends_down,
                            servers=servers,
                            backends=backends,
    )


@app.route("/servers_page", methods=['GET'])
def servers_page():

    servers = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        config.api_endpoint['SERVERS']), timeout=config.connection_timeout
    ).json()

    servers_up = [s for s in servers if s['status'] == 'UP']
    servers_down = [s for s in servers if s['status'] != 'UP']

    servers_up = len(servers_up)
    servers_down = len(servers_down)

    return render_template('servers_page.html',
                            servers_up=servers_up,
                            servers_down=servers_down,
                            servers=servers,
    )

@app.route("/backends_page", methods=['GET'])
def backends_page():

    backends = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        config.api_endpoint['BACKENDS']), timeout=config.connection_timeout
    ).json()
    
    backends_up = [b for b in backends if b['status'] == 'UP']
    backends_down = [b for b in backends if b['status'] != 'UP']

    backends_up = len(backends_up)
    backends_down = len(backends_down)

    return render_template('backends_page.html',
                            backends_up=backends_up,
                            backends_down=backends_down,
                            backends=backends,
    )    