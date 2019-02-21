from molinetes.ext.sql import db
from datetime import datetime

class Lectura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    credencial_id = db.Column(db.Integer,
                            db.ForeignKey('credencial.id'))
    molinete_id = db.Column(db.Integer,
                            db.ForeignKey('molinete.id'))
    evento_id = db.Column(db.Integer,
                           db.ForeignKey('evento.id'))

    def __repr__(self):
        return '<Lectura %r | %r>' % self.timestamp, self.credencial_id
