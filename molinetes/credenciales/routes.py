from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import Credencial, db

bp = Blueprint('credenciales', __name__)

@bp.route('/credenciales', methods=['GET'])
def list_all():

    status = 200
    credenciales = Credencial.query.all()
    res = [ {'name': c.nombre,
             'id': c.id } for c in credenciales ]

    return jsonify(res), status

@bp.route('/credenciales/<c_id>', methods=['GET'])
def list_one(c_id):

    status = 200
    c = Credencial.query.filter(Credencial.id==c_id).first()
    if c:
      res = { 'name': c.nombre, 'id': c.id }
    else:
        res = { 'msg': 'empty' }
        status = 204

    return jsonify(res), status

@bp.route('/credenciales', methods=['POST'])
def save_credenciales():

    if request.is_json:
        data = request.get_json()
        try:
            credencial  = Credencial(nombre = data['nombre'])
            db.session.add(credencial)
            db.session.commit()
            status = 201
            msg = "Its ok"
        except KeyError:
            msg = 'Params error'
            status = 400
    else:
        msg =  "Must to be json"
        status = 415

    return jsonify({'msg': msg }), status

@bp.route('/credenciales', methods=['PUT'])
def update():

    if request.is_json:

        data = request.get_json()
        c = Credencial.query.filter(Credencial.id==data['id']).first()
        if c:
            c.nombre = data['nombre']
            db.session.commit()
        else:
            status = 204


    res = {'name': c.nombre,
             'id': c.id }

    return jsonify(res)

@bp.route('/credenciales/<c_id>', methods=['DELETE'])
def delete(c_id):
    status = 200

    c = Credencial.query.filter(Credencial.id==c_id).first()
    if c:
        db.session.delete(c)
        db.session.commit()
        msg = {'msg': '{} deleted'.format(c_id)}
    else:
        status = 204
        msg = {'msg': 'No Content'}

    return jsonify(msg), status


