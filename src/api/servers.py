from flask_restplus import Resource
from base import api, STATUS_CODES
from haproxyadmin import *
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/servers", methods=['GET'])                                                                                                                   
class Servers(Resource):
    def get(self):

        servers = hap.servers()
        name, status, weight, requests, ip = [], [], [], [], []

        for server in servers:
            name.append(server.name)
            status.append(server.status)
            weight.append(server.weight)
            requests.append(server.requests)
            ip.append(server(address))

        response = [{"name": n,
                "status": s,
                "weight": w,
                "requests": r,
                "ip": ip,
                }
                for n, s, w, r, ip in zip(
                name,
                status,
                weight,
                requests,
                ip
                )
        ]
        return response