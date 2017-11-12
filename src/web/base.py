from flask import Flask, request

app = Flask(__name__)

STATUS_CODES = {
    200: 'Success.',
    400: 'Bad Request: only application/json is accepted.',
    422: 'Unprocessable Entity: json body contains semantic errors.'
}

