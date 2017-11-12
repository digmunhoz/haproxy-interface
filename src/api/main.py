from base import api
from base import app
import config
import api

if __name__ == '__main__':
    app.run(
        host=config.server_listen['ADDRESS'],
        port=config.server_listen['PORT'],
        use_reloader=False,
        debug=True
    )
