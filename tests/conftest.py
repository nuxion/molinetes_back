import pytest
from molinetes import create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app({
        'TESTING': True
    })
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
