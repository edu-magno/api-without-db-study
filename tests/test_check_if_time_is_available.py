from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
from app.services.check_if_time_is_available import check_if_time_is_available
import pytest


def test_check_if_time_is_available_is_false(clean_up_fixture):

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = check_if_time_is_available(file_path, fieldnames, 'Tue Sep 09 2020 10:52:13 GMT-0300 (-03)')
    expected = False

    assert expected == result


def test_check_if_time_is_available_is_true(clean_up_fixture):

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = check_if_time_is_available(file_path, fieldnames, 'Tue Sep 09 2020 11:52:13 GMT-0300 (-03)')
    expected = True

    assert expected == result
