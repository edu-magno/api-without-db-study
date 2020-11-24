from csv import DictReader
from json import dumps
from os import environ

def list_appointments() -> str:
    with open(environ.get('FILE_PATH'), 'r') as file:
        reader = list(DictReader(file))
        return dumps(reader)