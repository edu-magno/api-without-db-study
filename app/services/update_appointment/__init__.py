from typing import Dict
from csv import DictReader, DictWriter
from app.services.check_if_time_is_available import check_if_time_is_available
from app.services.user_id import user_id
from app.services.formatted_date import formatted_date
from os import environ
from re import search

def update_appointment(file_path, fieldnames, appointment: str, update: Dict) -> str:
    appointment_modified = {}
    list_appointments = []
    id_in_reader = False
    is_in_time_range = False

    if update.get('date'):
        update.update({'date': formatted_date(update['date'])})

    with open(file_path, 'r') as file:
        reader = DictReader(file, fieldnames=fieldnames)

        for appoint in reader:

            regex_date = search(r'[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}', update['date'])
            time = update['date'][regex_date.span()[0]:regex_date.span()[1]]

            hour = int(time[0:2])


            if appoint['id'] == appointment :
                id_in_reader = True
                if  8 <= hour <= 23:
                    appoint.update(update)
                    is_in_time_range = True
                    appointment_modified = appoint
                    list_appointments.append(appoint)
                    continue

            list_appointments.append(appoint)


    if id_in_reader == False:
        return {'message': 'O agendamento não existe.'}

    if is_in_time_range == False:
        return {'message': 'O horário está indisponível, os horários disponíveis são das 08:00 até as 23:00.'}

    if check_if_time_is_available(file_path, fieldnames, update['date']) == False:
        return {'message': 'O horário já está ocupado, tente outro horário entre 08:00-23:00.'}

    with open(file_path, 'w') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writerows(list_appointments)

    return appointment_modified
