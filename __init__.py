"""
The flask application package.
"""

from flask import Flask
from os import environ

app = Flask(__name__)

import view


if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 8000 
    app.run(HOST, PORT)
