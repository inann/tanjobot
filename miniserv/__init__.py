#!/usr/bin/python

from flask import Flask
from flask import request
import git
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # obviously, replace this.
        SECRET_KEY='a_real_secret_key',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello World!'

    @app.route('/newcommit', methods = ['GET', 'POST'])
    def fetch_and_pull():
        if request.method == 'GET':
            return 'Stub'
        else:
            return '👌Got \'em'

    return app