# You can use this to run flask run command like:
#   env FLASK_APP="cli.py" flask db init
#
import os
import click
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

@app.cli.command()
def populate_db():
    """Generate data."""

    # Crea las credenciales
    [ db.session.add(Credencial(nombre=x))
     for x in ['xavier', 'pepe', 'juan', 'rocio', 'julieta']]

    # Crea dos eventos
    db.session.add(Evento(nombre='ACDC', cod='20180701'))
    db.session.add(Evento(nombre='BocaVsRiver', cod='20170701'))

    db.session.commit()

    # Crea 3 molinetes dos asociados a un evento y 1 a otro.
    db.session.add(Molinete(evento_cod='20180701'))
    db.session.add(Molinete(evento_cod='20180701'))
    db.session.add(Molinete(evento_cod='20170701'))
    db.session.commit()



