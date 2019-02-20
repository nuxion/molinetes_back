from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import User, db

bp = Blueprint('users', __name__)

def make_dict(item):
    _dict = {
        'id': item.id,
        'email': item.email,
        'name': item.name,
        'password': item.password,
        'rol_id': item.rol_id
    }
    return _dict



@bp.route('/users', strict_slashes=False, methods=['GET'])
def list_all():
    status = 200
    users = User.query.all()
    if users:
        msg = list(map(make_dict, users))
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status


