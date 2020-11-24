from typing import Dict
from csv import DictReader, DictWriter
from app.services.check_if_time_is_available import check_if_time_is_available
from app.services.user_id import user_id
from app.services.formatted_date import formatted_date
from os import environ


def update_appointment(appointment: str, update: Dict) -> str:
    file_path = environ.get('FILE_PATH')
    fieldnames = [x for x in environ.get('FIELDNAMES').split(' ')]
    appointment_modified = {}
    list_appointments = []
    id_in_reader = False

    if update.get('date'):
        update.update({'date': formatted_date(update['date'])})

    with open(file_path, 'r') as file:
        reader = DictReader(file, fieldnames=fieldnames)

        for appoint in reader:

            if appoint['id'] == appointment:
                id_in_reader = True
                appoint.update(update)
                appointment_modified = appoint
                list_appointments.append(appoint)
                continue

            list_appointments.append(appoint)

    if id_in_reader == False:
        return {'message': 'O usuário não existe'}

    if check_if_time_is_available(update['date']) == False:
        return {'message': 'O horário já está ocupado, tente outro horário entre 08:00-23:00'}

    with open(file_path, 'w') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writerows(list_appointments)

    return appointment_modified
