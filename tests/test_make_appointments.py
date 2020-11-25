from app.services.make_appointments import make_appointments
from tests.variables_for_test_functions import *
from tests.clean_up_file import clean_up_file





def test_make_appointments_sucess():

    clean_up_file(file_path, fieldnames)



    result = make_appointments(file_path, fieldnames, appointment1)
    expected = appointment = {
        "id": 1,
        "date": "Tue Sep 09 2020 10:00:00 GMT-0300 (-03)",
        "name": "Son Goku",
        "school-subjects": "Matemática",
        "difficulty": "Não consegue entender como escalonar matrizes",
        "class-number": 3,
        "_growth": "Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes"
    }

    assert expected == result

def test_make_appointments_not_available_date():

    clean_up_file(file_path, fieldnames)

    make_appointments(file_path,fieldnames,appointment1)

    result = make_appointments(file_path,fieldnames,appointment4)
    expected = {'message': 'O horário já está ocupado, tente outro horário entre 08:00-23:00'}

    assert expected == result

def test_make_appointments_invalid_date():

    clean_up_file(file_path, fieldnames)

    result = make_appointments(file_path, fieldnames, appointment3)
    expected = {'message': 'Não foi possível marcar uma consulta nesse horário, as consultas só podem ser marcadas das 08:00 até as 23:00.'}

    assert expected == result