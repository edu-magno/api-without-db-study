from typing import Dict
from re import search
from csv import DictWriter
from app.services.user_id import user_id
from app.services.formatted_date import formatted_date
from app.services.check_if_time_is_available import check_if_time_is_available
from os import environ


def make_appointments(appointment: Dict) -> Dict:

    fieldnames = [x for x in environ.get('FIELDNAMES').split(' ')]
    file_path = environ.get('FILE_PATH')

    date = appointment['date']
    regex_date = search(r'[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}', date)
    time = date[regex_date.span()[0]:regex_date.span()[1]]

    hour = int(time[0:2])

    if check_if_time_is_available(date) == False:
        return {'message': 'O horário já está ocupado, tente outro horário entre 08:00-23:00'}

    if 8 <= hour <= 23:
        with open(file_path, 'a+') as file:

            writer = DictWriter(file, fieldnames=fieldnames)

            appointment.update({'id': user_id(file_path)})
            appointment.update({'date': formatted_date(date)})

            writer.writerow(appointment)

            return appointment

    return {'message': 'Não foi possível marcar uma consulta nesse horário, as consultas só podem ser marcadas das 08:00 até as 23:00.'}
