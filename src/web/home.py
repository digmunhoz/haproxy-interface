from flask import render_template
from base import app
import psutil

@app.route("/home", methods=['GET'])
def get():
    return render_template('index.html')
