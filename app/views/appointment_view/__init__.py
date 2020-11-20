from flask import Blueprint, request
from app.services.list_appointments import list_appointments
from app.services.make_appointments import make_appointments

bp = Blueprint('appointment', __name__)


@bp.route('/appointment', methods=['GET', 'POST'])
def list_and_make_appointments():
    if request.method == 'GET':
        return list_appointments()

    appointment = request.get_json()

    return make_appointments(appointment)
