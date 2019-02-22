from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.services import users
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('users', __name__)

@bp.route('/users', strict_slashes=False, methods=['GET'])
def list_all():
    status = 200
    users_all = users.find_all()
    if users_all:
        msg = { 'msg': users_all }
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status

@bp.route('/users/_login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({ 'msg': 'Missing username param'}), 400
    if not password:
        return jsonify({ 'msg': 'Missing password param'}), 400

    if users.validate_credentials(email, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@bp.route('/users/_logout', methods=['POST'])
@jwt_required
def logout():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    current_user = get_jwt_identity()
    if current_user == email:
        return jsonify(msg="{} logout".format(current_user)), 200
    else:
        return jsonify(msg='bad data'), 401




