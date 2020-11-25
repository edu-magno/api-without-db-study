from flask import Blueprint, request, jsonify
from app.services.list_appointments import list_appointments
from app.services.make_appointments import make_appointments
from os import environ

bp = Blueprint('appointment', __name__)


@bp.route('/appointment', methods=['GET', 'POST'])
def list_and_make_appointments():
    if request.method == 'GET':
        return jsonify(list_appointments(environ.get('FILE_PATH')))

    appointment = request.get_json()

    return make_appointments(environ.get('FILE_PATH'), [x for x in environ.get('FIELDNAMES').split(' ')] ,appointment)
