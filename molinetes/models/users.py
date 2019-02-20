import jwt
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    _password = db.Column("password", db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        """ I taked from
        https://docs.sqlalchemy.org/en/latest/orm/mapped_attributes.html
        """
        return self._password

    @password.setter
    def password(self, password):
        self._password = self.set_password(password)

    @staticmethod
    def set_password(password):
        """
        Password encrypt
        Maybe this method shall to be in a controller.
        :rturn: string
        """
        return generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email



class Rol(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User',
                            backref='users',
                            lazy=True)

    def __repr__(self):
        return '<Rol %r>' % self.name

