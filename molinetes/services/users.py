from werkzeug.security import check_password_hash, generate_password_hash
from molinetes.ext.sql import db
from molinetes.models import User

def make_dict(item):
    _dict = {
        'id': item.id,
        'email': item.email,
        'name': item.name,
        'rol_id': item.rol_id
    }
    return _dict


def find(email):
    """
    It gets the firts element that match with email.
    """
    return User.query.filter(User.email == email).first()

def find_all(_dict = False):

    users = User.query.all()
    response = list(map(make_dict, users))
    return response

def validate_credentials(username, password):
    u = find(username)
    if u:
        if check_password_hash(u.password, password):
            return True

    return False


