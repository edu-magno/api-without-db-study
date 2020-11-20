from typing import Dict
from csv import DictWriter
from json import dump


def update_appointment(appointment: int, update: Dict) -> str:

    fieldnames = ['id', 'date', 'name', 'school-subjects',
                  'difficulty', 'class-number', '_growth']

    with open('data/appointments.csv', 'w') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        appointment_modified = {}
        list_appointments = []
        for appoint in writer:
            if int(appoint['id']) == appointment:
                appoint.update(update)
                appointment_modified = appoint
                list_appointments.append(appoint)

            list_appointments.append(appoint)

        writer.writeheader()
        writer.writerows(list_appointments)
        return dump(appointment_modified)
