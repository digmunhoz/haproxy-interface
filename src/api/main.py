from base import api
from base import app
from flask_cors import CORS
import config

# Api endpoints
import backends
import errors
import frontends
import hardware
import info
import servers

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
#    app.run(
#        host=config.server_listen['ADDRESS'],
#        port=config.server_listen['PORT'],
#        use_reloader=False,
#        debug=True,
#        threaded=True
#    )
    app.run()
