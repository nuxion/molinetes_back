
def load_routes(app):
    prefix = app.config['URL_PREFIX']

    from . import root
    app.register_blueprint(root.bp, url_prefix='{}'.format(prefix))

    # add_routes # don't delete
    from .resources import users
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

