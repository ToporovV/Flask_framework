from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return f'This is a {request.method} request'

