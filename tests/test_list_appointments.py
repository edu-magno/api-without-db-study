from tests.clean_up_file import clean_up_file
from app.services.list_appointments import list_appointments
from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *



def test_list_appointments():

    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames,appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = list_appointments(file_path)
    expected = appointments_list

    assert expected == result
