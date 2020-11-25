from csv import DictReader
from os import environ

def list_appointments(file_path) -> str:
    with open(file_path, 'r') as file:
        reader = list(DictReader(file))
        return reader