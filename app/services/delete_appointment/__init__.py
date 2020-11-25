from csv import DictWriter, DictReader
from os import environ


def delete_appointment(file_path, fieldnames, appointment: str) -> str:

    id_in_reader = False
    list_appointments = []

    with open(file_path, 'r') as file:
        reader = DictReader(file, fieldnames=fieldnames)

        for appoint in reader:
            
            if appoint['id'] == appointment:
                id_in_reader = True
            if appoint['id'] != appointment:
                list_appointments.append(appoint)

    if id_in_reader == False:
        return {"error": "o agendamento não existe, tente novamente."}

    with open(file_path, 'w+') as file:
        writer = DictWriter(file, fieldnames=fieldnames)

        writer.writerows(list_appointments)
        return {'sucess': 'agendamento excluido!'}
