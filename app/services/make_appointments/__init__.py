from typing import Dict
from csv import DictWriter
from app.services.user_id import user_id
from app.services.formatted_date import formatted_date
from app.services.check_if_time_is_available import check_if_time_is_available
from os import environ
from app.services.get_hour import get_hour

def make_appointments(file_path, fieldnames, appointment: Dict) -> Dict:
    date = appointment['date']

    if check_if_time_is_available(file_path, fieldnames, date) == False:
        return {'message': 'O horário já está ocupado, tente outro horário entre 08:00-23:00'}

    if 8 <= get_hour(date) <= 23:
        with open(file_path, 'a+') as file:

            writer = DictWriter(file, fieldnames=fieldnames)

            appointment.update({'id': user_id(file_path)})
            appointment.update({'date': formatted_date(date)})

            writer.writerow(appointment)

            return appointment

    return {'message': 'Não foi possível marcar uma consulta nesse horário, as consultas só podem ser marcadas das 08:00 até as 23:00.'}
