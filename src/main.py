from base import app, api
import api.hardware
import api.information
import web.home
import config

if __name__ == '__main__':
    app.run(
        host=config.server_listen['ADDRESS'],
        port=config.server_listen['PORT'],
        use_reloader=False,
        debug=True
    )
