from flask import Blueprint, request, jsonify
from app.services.delete_appointment import delete_appointment
from app.services.update_appointment import update_appointment
from os import environ

bp = Blueprint('manipulate_appointments', __name__)


@bp.route('/appointment/<appointment_id>', methods=['PATCH', 'DELETE'])
def appointment(appointment_id):
    fieldnames = [x for x in environ.get('FIELDNAMES').split(' ')]
    if request.method == 'PATCH':
        appointment_request = request.get_json()
        return jsonify(update_appointment(environ.get('FILE_PATH'), fieldnames, appointment_id, appointment_request))

    return delete_appointment(environ.get('FILE_PATH'), fieldnames, appointment_id)
