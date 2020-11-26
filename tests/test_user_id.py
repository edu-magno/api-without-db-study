from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
from app.services.user_id import user_id
import pytest


def test_user_id():

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = user_id(file_path)
    expected = 3

    assert expected == result


def test_user_id_if_file_is_empty(clean_up_fixture):

    result = user_id(file_path)
    expected = 1

    assert expected == result
