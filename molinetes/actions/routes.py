from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import Lectura, db

bp = Blueprint('actions', __name__)

@bp.route('/actions/register', strict_slashes=False, methods=['POST'])
def register():

    if request.is_json:
        data = request.get_json()
        try:
            lectura  = Lectura(**data)
            db.session.add(lectura)
            db.session.commit()
            status = 201
            msg = "Its ok"
        except KeyError:
            msg = 'Params error'
            status = 400
    else:
        msg =  "The request MUST to be json"
        status = 415

    return jsonify({'msg': msg }), status

