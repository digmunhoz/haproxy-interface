from flask_restplus import Resource                                                                                                                           
from base import api, STATUS_CODES
from haproxyadmin import haproxy
import config
import psutil

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/v1/hardware", methods=['GET'])
class Hardware(Resource):
    def get(self):
        return {
             'mem': psutil.virtual_memory().percent,
             'cpu': psutil.cpu_percent()
        }
