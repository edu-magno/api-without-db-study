from flask import Blueprint, request, jsonify
from app.services.delete_appointment import delete_appointment
from app.services.update_appointment import update_appointment


bp = Blueprint('manipulate_appointments', __name__)


@bp.route('/appointment/<appointment_id>', methods=['PATCH', 'DELETE'])
def appointment(appointment_id):

    if request.method == 'PATCH':
        appointment_request = request.get_json()
        return jsonify(update_appointment(appointment_id, appointment_request))

    return delete_appointment(appointment_id)
