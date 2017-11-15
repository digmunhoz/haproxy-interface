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
        bname, brequests, bstatus, sname = [], [], [], []
        for backend in backends:
            bname.append(backend.name)
            brequests.append(backend.requests)                                                                                                                         
            bstatus.append(backend.status)
            servers = backend.servers()
            for server in servers:
                sname.append(server.name)

        response = [
            {
            "name": n, 
            "requests": r,
            "status": s, 
            # "servers": [ { "name": sn} for sn in zip (sname,) ]
            } 
            for n, r, s in zip(
            bname, 
            brequests,
            bstatus,
            )                
        ]

        return response