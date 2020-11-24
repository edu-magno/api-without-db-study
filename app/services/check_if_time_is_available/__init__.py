from app.services.formatted_date import formatted_date
from re import search
from csv import DictReader
from os import environ

def check_if_time_is_available(date: str) -> bool:

    with open(environ.get('FILE_PATH'), 'r') as file:
        reader = DictReader(file, fieldnames=[x for x in environ.get('FIELDNAMES').split(' ')])

        for appointment in reader:
            if appointment['date'] == formatted_date(date):
                return False

    return True
