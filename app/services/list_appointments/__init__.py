from csv import DictReader
from json import dumps


def list_appointments() -> str:
    with open('data/appointments.csv', 'r') as file:
        reader = list(DictReader(file))
        return dumps(reader)