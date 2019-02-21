import pytest
from molinetes.models import User, db

def test_create_user(test_client, init_db):

    user = User(email="nuxion@gmail.com",
                name="nuxion",
                password="test")

    db.session.add(user);
    db.session.commit()

    users = User.query.all()

    assert len(users) == 1
    assert users[0].password != 'test'

def test_create_duplicate(test_client, init_db):

    user = User(email="nuxion@gmail.com",
                name="nuxion",
                password="test")

    db.session.add(user);
    with pytest.raises(Exception):
        db.session.commit()

    db.session.rollback()
    users = User.query.all()

    assert len(users) == 1
