from csv import DictReader
from app.services.stringfied_date import stringfied_date
from re import search
from os import environ


def check_available_times(file_path, fieldnames, date: str):
    list_of_date_appointments = []
    hour_list = ['08:00:00', '09:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00',
                 '16:00:00', '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00']

    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:9])

    formatted_date = stringfied_date(day, month, year)

    with open(file_path, 'r') as file:
        reader = DictReader(
            file, fieldnames=fieldnames)

        for appointment in reader:

            appointment_date = appointment['date']

            if appointment_date.startswith(formatted_date):

                regex_date = search(
                    r'[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}', appointment_date)
                list_of_date_appointments.append(
                    appointment_date[regex_date.span()[0]:regex_date.span()[1]])

    list_of_available_appointments = [
        hour for hour in hour_list if hour not in list_of_date_appointments]

    return {'available-times': list_of_available_appointments}
