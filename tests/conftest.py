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

    url_prefix = '/api/v1'
    pytest.routes = {
        'users': '{}/users'.format(url_prefix),
    }

    flask_app = create_app({
        'TESTING': True,
        'SQLALCHEMY_TRACK_MODIFICATIONS' : False,
        'URL_PREFIX': url_prefix,
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
def token_access(test_client):
    url = '{}/_login'.format(pytest.routes['users'])
    response = test_client.post(url, json={
        'email': 'test@test.com', 'password': 'test'
    })
    token = response.json.get('access_token')
    print (token)

    yield token

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

