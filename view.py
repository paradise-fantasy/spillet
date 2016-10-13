"""
Routes and views for the flask application.
"""

from flask import Flask
from os import environ
import sys, re, os, random
from datetime import datetime
from flask import render_template, request, session, jsonify

app = Flask(__name__)


# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

@app.route('/')
def index():
    return 200

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 8000 
    app.run(HOST, PORT)
