from flask_restplus import Resource
from base import api, STATUS_CODES
import psutil

@api.route("/cpu", methods=['GET'])
class Cpu(Resource):

    def get(self):
        return psutil.cpu_percent()

@api.route("/mem", methods=['GET'])
class Mem(Resource):

    def get(self):
        return psutil.virtual_memory().percent
