import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from .models import db

__version__ = '0.2.dev'

#db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        URL_PREFIX = '/',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dev.db'\
        .format(app.instance_path),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    load_routes(app)

    return app

def load_routes(app):
    prefix = app.config['URL_PREFIX']

    from . import root
    app.register_blueprint(root.bp, url_prefix='{}'.format(prefix))

    # add_routes # don't delete
    from . import molinetes
    app.register_blueprint(molinetes.bp, url_prefix='{}'.format(prefix))

    from . import eventos
    app.register_blueprint(eventos.bp, url_prefix='{}'.format(prefix))

    from . import credenciales
    app.register_blueprint(credenciales.bp, url_prefix='{}'.format(prefix))

