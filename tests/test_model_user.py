import pytest
from molinetes.models import User

def test_create_user(test_client, init_db):

    user = User(email="nuxion@gmail.com",
                name="nuxion",
                password="test")

    init_db.session.add(user);
    init_db.session.commit()

    users = User.query.all()

    assert len(users) == 2
    assert users[1].password != 'test'

def test_create_duplicate(test_client, init_db):

    user = User(email="nuxion@gmail.com",
                name="nuxion",
                password="test")

    init_db.session.add(user);
    with pytest.raises(Exception):
        init_db.session.commit()

    init_db.session.rollback()
    users = User.query.all()

    assert len(users) == 2
