# Importing modules
from flask import render_template
import socket
import requests
# Importing files
from base import app
import config

@app.route("/home", methods=['GET'])
def home():

    hardware = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        '/api/hardware'), timeout=config.connection_timeout
    ).json()

    info = requests.get('http://{}:{}{}'.format( 
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        '/api/info'), timeout=config.connection_timeout
    ).json()

    servers = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        '/api/servers'), timeout=config.connection_timeout
    ).json()

    backends = requests.get('http://{}:{}{}'.format(
        config.api_server['ADDRESS'], 
        config.api_server['PORT'], 
        '/api/backends'), timeout=config.connection_timeout
    ).json()

    servers_up = [s for s in servers if s['status'] == 'UP']
    servers_down = [s for s in servers if s['status'] != 'UP']
    
    backends_up = [b for b in backends if b['status'] == 'UP']
    backends_down = [b for b in backends if b['status'] != 'UP']

    cpu = hardware['cpu']
    mem = hardware['mem']
    currconns = info[0]['CurrConns']
    version = info[0]['Version']
    node = info[0]['node']
    uptime = info[0]['Uptime']
    ulimitn = info[0]['Ulimit-n']    
    maxconn = int(info[0]['Hard_maxconn'])
    maxsessrate = int(info[0]['MaxSessRate'])
    sessrate = int(info[0]['SessRate'])
    maxconn = '{0:,}'.format(maxconn).replace(',','.')
    servers_up = len(servers_up)
    servers_down = len(servers_down)
    backends_up = len(backends_up)
    backends_down = len(backends_down)    
    return render_template('home.html', 
                            cpu=cpu, 
                            mem=mem,
                            currconns=currconns,
                            version=version,
                            maxconn=maxconn,
                            uptime=uptime,
                            node=node,
                            servers_up=servers_up,
                            servers_down=servers_down,
                            backends_up=backends_up,
                            backends_down=backends_down,
                            sessrate=sessrate,
                            ulimitn=ulimitn
    )
