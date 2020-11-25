from flask import Blueprint, request
from app.services.check_available_time_on_the_day import check_available_times
from os import environ
bp = Blueprint('available_times_on_the_day', __name__)


@bp.route('/appointment/available_times_on_the_day', methods=['GET'])
def available_times():
    query_params = request.args

    return check_available_times(environ.get('FILE_PATH'), [x for x in environ.get('FIELDNAMES').split(' ')], query_params['date'])
