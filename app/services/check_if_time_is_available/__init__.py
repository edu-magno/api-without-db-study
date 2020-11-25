from app.services.formatted_date import formatted_date
from re import search
from csv import DictReader
from os import environ

def check_if_time_is_available(file_path, fieldnames, date: str) -> bool:

    with open(file_path, 'r') as file:
        reader = DictReader(file, fieldnames=fieldnames)

        for appointment in reader:
            if appointment['date'] == formatted_date(date):
                return False

    return True
