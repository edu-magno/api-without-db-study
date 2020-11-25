from tests.clean_up_file import clean_up_file
from app.services.make_appointments import make_appointments
from app.services.user_id import user_id
from tests.variables_for_test_functions import *


def test_user_id():
    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = user_id(file_path)
    expected = 3

    assert expected == result


def test_user_id_if_file_is_empty():
    clean_up_file(file_path, fieldnames)

    result = user_id(file_path)
    expected = 1

    assert expected == result