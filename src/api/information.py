from flask_restplus import Resource                                                                                                                           
from base import api, STATUS_CODES
from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_dir='/tmp',socket_file='stats')

@api.route("/api/info", methods=['GET'])
class Info(Resource):

    def get(self):
        return hap.info()

@api.route("/api/errors", methods=['GET'])
class Errors(Resource):

    def get(self):
        return hap.errors()
