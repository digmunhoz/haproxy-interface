from flask import Flask, redirect
from base import app
import dashboard
import servers
import config

@app.route('/')
def hello():
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(
        host=config.server_listen['ADDRESS'],
        port=config.server_listen['PORT'],
        use_reloader=False,
        debug=True,
	threaded=True
    )
