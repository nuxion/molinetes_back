#from molinetes.models import db
from . import db

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.String(80))
    nombre = db.Column(db.String(80))
    molinetes = db.relationship('Molinete',
                                backref='evento',
                                lazy=True)
    credenciales = db.relationship('Credencial',
                                backref='evento')

    def __repr__(self):
        return '<Evento %r>' % self.nombre
