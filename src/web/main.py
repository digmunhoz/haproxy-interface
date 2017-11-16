from base import app
import dashboard
import servers
import config

if __name__ == '__main__':
    app.run(
        host=config.server_listen['ADDRESS'],
        port=config.server_listen['PORT'],
        use_reloader=False,
        debug=True,
	threaded=True
    )
