___
to: <%= dir_name %>/root/routes.py
___
from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )

bp = Blueprint('root', __name__)

@bp.route('/', methods=['GET'])
def simple_response():
    return jsonify({'msg': 'its ok'})

