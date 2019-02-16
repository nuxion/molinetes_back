---
to: <%= dir_name %>/__init__.py
---
import os
from flask import Flask

__version__ = '0.1.dev'

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        URL_PREFIX = '/'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    load_routes(app)

    return app

def load_routes(app):
    from . import root
    #import pdb; pdb.set_trace()
    # add routes

    prefix = app.config['URL_PREFIX']

    app.register_blueprint(root.bp, url_prefix='{}'.format(prefix))




