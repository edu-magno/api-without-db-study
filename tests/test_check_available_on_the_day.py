from tests.clean_up_file import clean_up_file
from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
from app.services.check_available_time_on_the_day import check_available_times


def test_check_available_times():
    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment5)

    result = check_available_times(file_path, fieldnames, '09092020')

    expected = {"available-times": ["08:00:00", "09:00:00","11:00:00", "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00", "19:00:00", "20:00:00", "21:00:00", "22:00:00", "23:00:00"]}

    assert expected == result
