from csv import DictWriter, DictReader
from os import environ


def delete_appointment(appointment: int) -> str:
    file_path = environ.get('FILE_PATH')
    fieldnames = [x for x in environ.get('FIELDNAMES').split(' ')]
    id_in_reader = False
    list_appointments = []

    with open(file_path, 'r') as file:
        reader = DictReader(file, fieldnames=fieldnames)

        for appoint in reader:
            print(appoint)
            if appoint['id'] == appointment:
                id_in_reader = True
            if appoint['id'] != appointment:
                list_appointments.append(appoint)

    if id_in_reader == False:
        return {"error": "appointment doesn't exist"}

    with open(file_path, 'w+') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        print(list_appointments)
        writer.writerows(list_appointments)
        return {'sucess': 'appointment deleted'}
