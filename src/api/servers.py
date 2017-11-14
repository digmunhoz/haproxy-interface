from flask_restplus import Resource
from base import api, STATUS_CODES
from haproxyadmin import haproxy
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/servers", methods=['GET'])                                                                                                                   
class Servers(Resource):
    def get(self):
        servers = hap.servers()
        name, status, weight, requests = [], [], [], []

        for server in servers:
            name.append(server.name)

        for server in servers:
            status.append(server.status)

        for server in servers:
            weight.append(server.weight)

        for server in servers:
            requests.append(server.requests)

        response = [{"name": n,
                "status": s,
                "weight": w,
                "requests": r,
                }
                for n, s, w, r in zip(
                name,
                status,
                weight,
                requests
                )
        ]
        return response
