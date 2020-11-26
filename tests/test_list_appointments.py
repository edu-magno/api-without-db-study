from app.services.list_appointments import list_appointments
from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
import pytest


def test_list_appointments(clean_up_fixture):

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = list_appointments(file_path)
    expected = appointments_list

    assert expected == result
