#from molinetes.models import db
from . import db

class Molinete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_cod = db.Column(db.String(80),
                           db.ForeignKey('evento.cod'))
    credenciales = db.relationship('Credencial',
                                   backref='credencial',
                                   lazy=True)

    def __repr__(self):
        return '<Molinete %r>' % self.id
