# Importing modules
from flask import render_template
import socket
import requests
# Importing files
from base import app
import config

@app.route("/home", methods=['GET'])
def home():
    hardware = requests.get('http://' + 
                            config.api_server['ADDRESS'] + ':' + 
                            config.api_server['PORT'] + 
                            '/api/hardware', 
                            timeout=config.connection_timeout
    ).json()
    info = requests.get('http://' + 
                        config.api_server['ADDRESS'] + ':' + 
                        config.api_server['PORT'] + 
                        '/api/info', 
                        timeout=config.connection_timeout
    ).json()
    servers = requests.get('http://' + 
                        config.api_server['ADDRESS'] + ':' + 
                        config.api_server['PORT'] + 
                        '/api/servers', 
                        timeout=config.connection_timeout
    ).json()
    servers_up = [x for x in servers if x['status'] == 'UP']
    servers_down = [x for x in servers if x['status'] != 'UP']
    
    cpu = hardware['cpu']
    mem = hardware['mem']
    currconns = info[0]['CurrConns']
    version = info[0]['Version']
    name = info[0]['Name']
    uptime = info[0]['Uptime']
    maxconn = int(info[0]['Hard_maxconn'])
    maxconn = '{0:,}'.format(maxconn).replace(',','.')
    servers_up = len(servers_up)
    servers_down = len(servers_down)
    return render_template('home.html', 
                            cpu=cpu, 
                            mem=mem,
                            currconns=currconns,
                            version=version,
                            maxconn=maxconn,
                            uptime=uptime,
                            name=name,
                            servers_up=servers_up,
                            servers_down=servers_down
    )
