from tests.variables_for_test_functions import file_path, fieldnames, appointment1, appointment2
from app.services.make_appointments import make_appointments
from csv import DictWriter
import pytest


def clean_up_file(file_path, fieldnames):
    with open(file_path, 'w') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


# def clean_up_file_and_make_two_appointments(file_path, fieldnames):
#      with open(file_path, 'w') as file:
#         writer = DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()

#         make_appointments(file_path, fieldnames, appointment1)
#         make_appointments(file_path, fieldnames, appointment2)


@pytest.fixture()
def clean_up_fixture():
    clean_up_file(file_path, fieldnames)

# @pytest.fixture()
# def clean_up_and_make_appointments_fixture():
#     clean_up_file_and_make_two_appointments(file_path, fieldnames)
