from tests.clean_up_file import clean_up_file
from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
from app.services.list_appointments import list_appointments
from app.services.delete_appointment import delete_appointment


def test_delete_appointment():
    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    delete_appointment(file_path, fieldnames, '1')

    result = list_appointments(file_path)
    expected = [{
        'id': "2",
        'date': 'Tue Sep 09 2020 08:00:00 GMT-0300 (-03)',
        'name': 'Marquinhos DJ',
        'school-subjects': 'Física',
        'difficulty': 'Não está entendendo a teoria de newton',
        'class-number': "3",
        '_growth': 'Agora o aluno entendeu sobre a teoria de newton'
    }]

    assert expected == result


def test_return_of_delete_appointment():
    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = delete_appointment(file_path, fieldnames, '1')
    expected = {'sucess': 'agendamento excluido!'}

    assert expected == result


def test_return_of_delete_appointment_if_apppointment_doesnt_exist():
    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = delete_appointment(file_path, fieldnames, '1')
    expected = {"error": "o agendamento não existe, tente novamente."}
