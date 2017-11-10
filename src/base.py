from flask import Flask, request
from flask_restplus import Api

app = Flask(__name__)
api = Api(app, title='HAProxy Interface', doc='/doc/')

STATUS_CODES = {
    200: 'Success.',
    400: 'Bad Request: only application/json is accepted.',
    422: 'Unprocessable Entity: json body contains semantic errors.'
}

