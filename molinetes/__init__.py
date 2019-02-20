import os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
#from flask_sqlalchemy import SQLAlchemy
from .models import db
from .auth import jwt

__version__ = '0.2.dev'

#db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        URL_PREFIX = '/api/v1/',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dev.db'\
        .format(app.instance_path),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    cors = CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    load_routes(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error=404, text=str(e)), 404

    return app

def load_routes(app):
    prefix = app.config['URL_PREFIX']

    from . import root
    app.register_blueprint(root.bp, url_prefix='{}'.format(prefix))

    # add_routes # don't delete
    from . import users
    app.register_blueprint(users.bp, url_prefix='{}'.format(prefix))

    from . import auth
    app.register_blueprint(auth.bp, url_prefix='{}'.format(prefix))

    from . import lecturas
    app.register_blueprint(lecturas.bp, url_prefix='{}'.format(prefix))

    from . import actions
    app.register_blueprint(actions.bp,
                           url_prefix='{}actions'.format(prefix))

    from . import molinetes
    app.register_blueprint(molinetes.bp, url_prefix='{}'.format(prefix))

    from . import eventos
    app.register_blueprint(eventos.bp, url_prefix='{}'.format(prefix))

    from . import credenciales
    app.register_blueprint(credenciales.bp, url_prefix='{}'.format(prefix))

