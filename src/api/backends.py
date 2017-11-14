from flask_restplus import Resource                                                                                                                           
from base import api, STATUS_CODES
from haproxyadmin import haproxy
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/backends", methods=['GET'])
class Backends(Resource):
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
