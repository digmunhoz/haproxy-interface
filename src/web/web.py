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
    cpu = hardware['cpu']
    mem = hardware['mem']
    currconns = info[0]['CurrConns']
    version = info[0]['Version']
    maxconn = int(info[0]['Hard_maxconn'])
    maxconn = '{0:,}'.format(maxconn).replace(',','.')
    return render_template('home.html', 
                            cpu=cpu, 
                            mem=mem,
                            currconns=currconns,
                            version=version,
                            maxconn=maxconn,
    )
