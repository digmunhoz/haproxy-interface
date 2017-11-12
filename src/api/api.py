from flask_restplus import Resource
from base import api, STATUS_CODES
from haproxyadmin import haproxy
import config
import psutil
import json

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/hardware", methods=['GET'])
class Hardware(Resource):
    def get(self):
        return {
             'mem': psutil.virtual_memory().percent,
             'cpu': psutil.cpu_percent()
        }

@api.route("/api/info", methods=['GET'])
class Info(Resource):
    def get(self):
        return hap.info()

@api.route("/api/errors", methods=['GET'])
class Errors(Resource):
    def get(self):
        return hap.errors()

@api.route("/api/backends", methods=['GET'])
class Ends(Resource):
    def get(self):

        backends = hap.backends()
        name, requests, status = [], [], []

        for backend in backends:
            name.append(backend.name)

        for backend in backends:
            requests.append(backend.requests)

        for backend in backends:                                                                                                                              
            status.append(backend.status)

        response = [{"name": n, 
                "requests": r,
                "status": s,
                } 
                for n, r, s in zip(
                name, 
                requests,
                status
                )
        ]

        return response

@api.route("/api/frontends", methods=['GET'])
class Ends(Resource):
    def get(self):
        frontends = hap.frontends()
        name, requests, status, maxconn = [], [], [], []

        for frontend in frontends:
            name.append(frontend.name)

        for frontend in frontends:
            requests.append(frontend.requests)

        for frontend in frontends:                                                                                                      
            status.append(frontend.status)

        for frontend in frontends:                                                                                                      
            maxconn.append(frontend.maxconn)

        response = [{"name": n, 
                "requests": r,
                "status": s,
                "maxconn": m,
                } 
                for n, r, s, m in zip(
                name, 
                requests,
                status,
                maxconn
                )
        ]
        return response
