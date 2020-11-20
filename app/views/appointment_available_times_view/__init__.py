from flask import Blueprint, request
from app.services.check_available_date import check_available_date

bp = Blueprint('available_times_on_the_day', __name__)


@bp.route('/appointment/available_times_on_the_day', methods=['GET'])
def available_times():
    date = request.args

    return check_available_date(date)
