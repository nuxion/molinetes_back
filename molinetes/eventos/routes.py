from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import Evento, db

bp = Blueprint('eventos', __name__)

def make_cred(item):
    _dict = {'id': item.id,
             'nombre': item.nombre,
             'molinete': item.molinete_id}
    return _dict

def make_molinete(item):
    _dict = {'id': item.id }
    return _dict

def make_dict(item):
    _dict = {
        'id': item.id,
        'cod': item.cod,
        'nombre': item.nombre,
        'molinetes': list(map(make_molinete, item.molinetes)),
        'credenciales': list(map(make_cred, item.credenciales))
    }
    return _dict

@bp.route('/eventos', strict_slashes=False, methods=['GET'])
def list_all():
    status = 200
    eventos = Evento.query.all()
    if eventos:
        msg = list(map(make_dict, eventos))
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status

@bp.route('/eventos/<id>', methods=['GET'])
def list_one(id):
    status = 200
    e = Evento.query.filter(Evento.id==id).first()
    if e:
        msg = make_dict(e)
    else:
        msg = { 'msg': 'empty' }
        status = 204

    return jsonify(msg), status

@bp.route('/eventos', methods=['POST'])
def create():

    if request.is_json:
        data = request.get_json()
        try:
            evento  = Evento(**data)
            db.session.add(evento)
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

@bp.route('/eventos/<id>', methods=['PUT'])
def update(id):

    status = 200
    if request.is_json:
        data = request.get_json()
        e = Evento.query.filter(Evento.id==id)
        if e:
            e.update(data)
            db.session.commit()
            msg = {'msg': 'id: {} updated'.format(id)}
        else:
            status = 204
            msg = {'msg': 'The id {} not exist'.format(id)}

    return jsonify(msg), status

@bp.route('/eventos/<id>', methods=['DELETE'])
def delete(id):
    status = 200

    e = Evento.query.filter(Evento.id==id).first()
    if e:
        db.session.delete(e)
        db.session.commit()
        msg = {'msg': '{} deleted'.format(id)}
    else:
        status = 204
        msg = {'msg': 'No content for {}'.format(id)}

    return jsonify(msg), status
