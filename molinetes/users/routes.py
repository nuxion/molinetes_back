from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from services import Users
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('users', __name__)

@bp.route('/users', strict_slashes=False, methods=['GET'])
def list_all():
    status = 200
    users = Users.find_all()
    if users:
        msg = { 'msg': users }
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status

@bp.route('/users/login', strict_slashes=False, methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({ 'msg': 'Missing username param'}), 400
    if not password:
        return jsonify({ 'msg': 'Missing password param'}), 400

    if Users.validate_credentials(email, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


