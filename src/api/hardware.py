from flask_restplus import Resource
from base import api, STATUS_CODES
import psutil

@api.route("/api/hardware", methods=['GET'])
class Hardware(Resource):

    def get(self):
        return {
             'mem': psutil.virtual_memory().percent,
             'cpu': psutil.cpu_percent()
        }
