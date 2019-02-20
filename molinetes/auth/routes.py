from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from werkzeug.security import check_password_hash, generate_password_hash
from molinetes.models import User, db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity


bp = Blueprint('auth', __name__)

def validate_credentials(username, password):
    u = User.query.filter(User.email == username).first()
    if u:
        if check_password_hash(u.password, password):
            return True

    return False

@bp.route('/actions/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({ 'msg': 'Missing username param'}), 400
    if not password:
        return jsonify({ 'msg': 'Missing password param'}), 400

    if validate_credentials(email, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@bp.route('/actions/testlogin', methods=['GET'])
@jwt_required
def test_login():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
