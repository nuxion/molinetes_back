___
to: <%= h.package %>/<%= name %>/routes.py
___
from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )

bp = Blueprint('<%= name %>', __name__)

@bp.route('/<%= name %>', methods=['GET'])
def simple_response():
    return jsonify({'msg': '<%= name %>'})

