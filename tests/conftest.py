from __future__ import absolute_import
import os
import sys
import pytest
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from molinetes import create_app
from molinetes.models import Credencial, User
from molinetes.ext.sql import db



@pytest.fixture(scope='module')
def test_client():
    pytest.url_prefix = '/api/v1'

    flask_app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI' : 'sqlite:///test.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS' : False,
        'URL_PREFIX': pytest.url_prefix,
        'SECRET_KEY': 'testing'
    })
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/test.db'\
        .format(flask_app.instance_path)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope='module')
def init_db():
    # Create the database and the database table
    db.drop_all()
    db.create_all()

    # Insert user data
    c1 = Credencial(nombre='test1')
    c2 = Credencial(nombre='test2')
    db.session.add(c1)
    db.session.add(c2)

    # Commit the changes for the users
    db.session.commit()

    u = User(email="test@test.com", password="test")
    db.session.add(u)
    db.session.commit()
    yield db  # this is where the testing happens!

    db.drop_all()

