import pytest
from molinetes import create_app
from molinetes.models import db, Credencial



@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI' : 'sqlite:///test.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS' : False
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
    db.create_all()

    # Insert user data
    c1 = Credencial(nombre='test1')
    c2 = Credencial(nombre='test2')
    db.session.add(c1)
    db.session.add(c2)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()

