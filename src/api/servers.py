from flask_restplus import Resource
from base import api, STATUS_CODES
from haproxyadmin import *
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/v1/servers", methods=['GET'])                                                                                                                   
class Servers(Resource):
    def get(self):

        servers = hap.servers()
        name, status, weight, requests, backend, scur, smax = [], [], [], [], [], [], []

        for server in servers:
            name.append(server.name)
            status.append(server.status)
            weight.append(server.weight)
            scur.append(server.metric('scur'))
            smax.append(server.metric('smax'))
            requests.append(server.requests)
            backend.append(server.backendname)

        response = [{"name": n,
                "status": s,
                "weight": w,
                "requests": r,
                "backend": be,
                "scur": scur,
                "smax": smax,
                }
                for n, s, w, r, be, scur, smax in zip(
                name,
                status,
                weight,
                requests,
                backend,
                scur,
                smax,
                )
        ]
        return response