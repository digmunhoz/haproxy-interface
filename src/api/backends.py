from flask_restplus import Resource                                                                                                                           
from base import api, STATUS_CODES
from haproxyadmin import *
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/v1/backends", methods=['GET'])
class Backends(Resource):
    def get(self):

        backends = hap.backends()
        bname, scur, bstatus, qcur, smax = [], [], [], [], []
        for backend in backends:
            bname.append(backend.name)
            scur.append(backend.metric('scur'))
            smax.append(backend.metric('smax'))                                                                                                                        
            bstatus.append(backend.status)
            qcur.append(backend.metric('qcur'))

        response = [
            {
            "name": n, 
            "scur": scur,
            "smax": smax,
            "status": s,
            "qcur": qcur,
            } 
            for n, scur, smax, s, qcur in zip(
            bname, 
            scur,
            smax,
            bstatus,
            qcur,
            )                
        ]

        return response


@api.route("/api/v2/backends", methods=['GET'])
class Backends(Resource):
    def get(self):

        backends = hap.backends()
        result = {'backends':[]}
        sb = 0
        for backend in backends:
            result['backends'].append({ 'name': backend.name, 'servers':[] })
            ss = 0
            for server in backend.servers():
                result['backends'][sb]['servers'].append({'name': server.name, 'parameters':{}})
                for m in SERVER_METRICS:
                    result['backends'][sb]['servers'][ss]['parameters'].update({m: server.metric(m)})
                ss += 1
            sb += 1

        return [result]