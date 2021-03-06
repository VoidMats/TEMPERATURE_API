#! /bin/python3

import os

from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['JWT_BLACKLIST_ENABLED'] = False
    #app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    #app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['VERSION'] = '0.0.1'
    print("----- Instantiate TEMPERATURE API -----")

    if config_name:
        app.config.from_object(config[config_name])
        print(" * Loading {} configuration...".format(config_name))
    else:
        app.config.from_object(config['development'])
        print(" * Loading development configuration ...")
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)

    with app.app_context():
        from app import routes
        from app import db_sqlite
        from app import apiexception

        return app
