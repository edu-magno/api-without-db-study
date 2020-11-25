from tests.clean_up_file import clean_up_file
from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
from app.services.update_appointment import update_appointment


def test_update_appointment():
    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment1)

    result = update_appointment(file_path, fieldnames, '1', {
                                'date': 'Tue Sep 09 2020 11:54:11 GMT-0300 (-03)'})
    expected = {
        "id":"1",
        'date': 'Tue Sep 09 2020 11:00:00 GMT-0300 (-03)',
        'name': 'Son Goku',
        'school-subjects': 'Matemática',
        'difficulty': 'Não consegue entender como escalonar matrizes',
        'class-number': '3',
        '_growth': 'Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes'
    }

    assert expected == result

def test_update_appointment_if_date_not_available():

    clean_up_file(file_path, fieldnames)

    make_appointments(file_path, fieldnames, appointment1)
    make_appointments(file_path, fieldnames, appointment2)

    result = update_appointment(file_path, fieldnames, '2', {'date':'Tue Sep 09 2020 10:52:13 GMT-0300 (-03)'})
    expected = {'message': 'O horário já está ocupado, tente outro horário entre 08:00-23:00'}

    assert expected == result

