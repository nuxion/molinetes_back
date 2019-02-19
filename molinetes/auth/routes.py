from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )

bp = Blueprint('auth', __name__)

@bp.route('/auth', methods=['GET'])
def simple_response():
    return jsonify({'msg': 'auth'})

