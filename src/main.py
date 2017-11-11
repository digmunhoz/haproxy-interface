from base import app, api
import api.hardware
import api.information
import web.home
import config

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        use_reloader=False,
        debug=True
    )
