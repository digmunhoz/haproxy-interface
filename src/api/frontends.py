from flask_restplus import Resource
from base import api, STATUS_CODES
from haproxyadmin import haproxy
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/frontends", methods=['GET'])                                                                                                                 
class Frontends(Resource):
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
