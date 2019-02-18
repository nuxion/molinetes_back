from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import Credencial, db

bp = Blueprint('credenciales', __name__)

def make_dict(item):
    """
    It takes a row object from SQLAlchemy query response
    and makes a dict object that will be serialized to json.
    """
    _dict = { 'id': item.id,
             'nombre': item.nombre,
             'molinete': item.molinete_id
              }
    try:
        _dict.update({ 'evento': item.evento.nombre })
    except AttributeError:
        _dict.update({ 'evento': None})

    return _dict

@bp.route('/credenciales', strict_slashes=False, methods=['GET'])
def list_all():

    status = 200
    credenciales = Credencial.query.all()
    if credenciales:
        """msg = [ {'nombre': c.nombre,
                'evento': c.evento.nombre,
                'molinete': c.molinete_id,
                'id': c.id } for c in credenciales ]"""
        msg = list(map(make_dict, credenciales))
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status

@bp.route('/credenciales/<c_id>', methods=['GET'])
def list_one(c_id):

    status = 200
    c = Credencial.query.filter(Credencial.id==c_id).first()
    if c:
      res = { 'name': c.nombre,
             'evento': c.evento.nombre,
             'molinete': c.molinete_id,
             'id': c.id }
    else:
        res = { 'msg': 'empty' }
        status = 204

    return jsonify(res), status

@bp.route('/credenciales', methods=['POST'])
def create():

    if request.is_json:
        data = request.get_json()
        try:
            #credencial  = Credencial(nombre = data['nombre'])
            credencial  = Credencial(**data)
            db.session.add(credencial)
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

@bp.route('/credenciales/<id>', methods=['PUT'])
def update(id):

    status = 200

    if request.is_json:

        data = request.get_json()
        c = Credencial.query.filter(Credencial.id==id)
        if c:
            c.update(data)
            db.session.commit()
            msg = {'msg': 'id: {} updated'.format(id)}
        else:
            status = 204
            msg = {'msg': 'The id {} not exist'.format(id)}

    return jsonify(msg), status

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
        msg = {'msg': 'No content for {}'.format(c_id)}

    return jsonify(msg), status
