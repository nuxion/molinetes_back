#from molinetes.models import db
from . import db

class Credencial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))

    def __repr__(self):
        return '<Credencial %r' % self.nombre
