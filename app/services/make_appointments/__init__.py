from typing import Dict
from csv import DictWriter
from app.services.user_id import user_id


def make_appointments(appointment: Dict) -> Dict:
    fieldnames = ['id', 'date', 'name', 'school-subjects',
                  'difficulty', 'class-number', '_growth']
    file_path = 'data/appointments.csv'

    with open(file_path, 'a+') as file:
        writer = DictWriter(file, fieldnames=fieldnames)

        appointment.update({'id': user_id(file_path)})
        
        writer.writerow(appointment)

        return appointment
