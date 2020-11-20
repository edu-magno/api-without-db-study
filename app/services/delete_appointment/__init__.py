from csv import DictWriter


def delete_appointment(appointment: int) -> str:

    fieldnames = ['id', 'date', 'name', 'school-subjects',
                  'difficulty', 'class-number', '_growth']

    with open('data/appointments.csv', 'w') as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        list_appointments = []
        for appoint in writer:
            if int(appoint['id']) != appointment:
                list_appointments.append(appoint)

        writer.writeheader()
        writer.writerows(list_appointments)

        return 'appointment deleted'
