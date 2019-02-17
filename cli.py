# You can use this to run flask run command like:
#   env FLASK_APP="cli.py" flask db init
#
import os
from molinetes import create_app
from molinetes.models import db, Evento, Molinete, Credencial
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=db,
                Credencial=Credencial,
                Evento=Evento,
                Molinete=Molinete
                )


