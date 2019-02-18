from flask import (
    Blueprint, g, redirect, request, session, url_for, jsonify )
from molinetes.models import Molinete, db

bp = Blueprint('molinetes', __name__)

def make_cred(item):
    _dict = {'id': item.id,
             'nombre': item.nombre,
             'molinete': item.molinete_id}
    return _dict

def make_dict(item):
    _dict = {
        'id': item.id,
        'evento_cod': item.evento_cod,
        'credenciales': list(map(make_cred, item.credenciales))
    }
    return _dict

@bp.route('/molinetes', strict_slashes=False, methods=['GET'])
def list_all():
    status = 200
    molinetes = Molinete.query.all()
    if molinetes:
        msg = list(map(make_dict, molinetes))
    else:
        status= 204
        msg = {'msg': 'empty'}

    return jsonify(msg), status

@bp.route('/molinetes/<id>', methods=['GET'])
def list_one(id):
    status = 200
    m = Molinete.query.filter(Molinete.id==id).first()
    if m:
        msg = make_dict(m)
    else:
        msg = { 'msg': 'empty' }
        status = 204

    return jsonify(msg), status

@bp.route('/molinetes', strict_slashes=False, methods=['POST'])
def create():

    if request.is_json:
        data = request.get_json()
        try:
            molinete  = Molinete(**data)
            db.session.add(molinete)
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

@bp.route('/molinetes/<id>', methods=['PUT'])
def update(id):

    status = 200
    if request.is_json:
        data = request.get_json()
        m = Molinete.query.filter(Molinete.id==id)
        if m:
            m.update(data)
            db.session.commit()
            msg = {'msg': 'id: {} updated'.format(id)}
        else:
            status = 204
            msg = {'msg': 'The id {} not exist'.format(id)}

    return jsonify(msg), status

@bp.route('/molinetes/<id>', methods=['DELETE'])
def delete(id):
    status = 200

    e = Molinete.query.filter(Molinete.id==id).first()
    if e:
        db.session.delete(e)
        db.session.commit()
        msg = {'msg': '{} deleted'.format(id)}
    else:
        status = 204
        msg = {'msg': 'No content for {}'.format(id)}

    return jsonify(msg), status
