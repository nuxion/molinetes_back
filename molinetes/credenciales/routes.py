from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )

bp = Blueprint('credenciales', __name__)

@bp.route('/credenciales', methods=['GET'])
def simple_response():
    return jsonify({'msg': 'credenciales'})

