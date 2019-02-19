from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import Lectura, db

bp = Blueprint('lecturas', __name__)

def make_dict(item):
    _dict = {
        'id': item.id,
        'timestamp': item.timestamp,
        'credencial_id': item.credencial_id,
        'evento_id': item.evento_id,
        'molinete_id': item.molinete_id
    }
    return _dict

@bp.route('/lecturas', strict_slashes=False, methods=['GET'])
def list_all():
    status = 200
    lecturas = Lectura.query.all()
    if lecturas:
        msg = list(map(make_dict, lecturas))
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status

