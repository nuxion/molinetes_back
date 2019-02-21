from molinetes.ext.sql import db

class Credencial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))

    molinete_id = db.Column(db.Integer,
                            db.ForeignKey('molinete.id'))
    evento_cod = db.Column(db.String(80),
                           db.ForeignKey('evento.cod'))

    def __repr__(self):
        return '<Credencial %r' % self.nombre
