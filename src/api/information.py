from flask_restplus import Resource                                                                                                                           
from base import api, STATUS_CODES
from haproxyadmin import haproxy
import config

hap = haproxy.HAProxy(
    socket_dir=config.haproxy_socket['DIR'],
    socket_file=config.haproxy_socket['FILE']
)

@api.route("/api/info", methods=['GET'])
class Info(Resource):

    def get(self):
        return hap.info()

@api.route("/api/errors", methods=['GET'])
class Errors(Resource):

    def get(self):
        return hap.errors()
