from csv import DictReader

def user_id(filename: str):
    with open(filename, 'r', newline='') as file:
        reader = DictReader(file)

        list_reader = list(reader)

        if list_reader == []:
            return 1

        id_of_last_line = list_reader[-1].get('id', 0)
        return int(id_of_last_line) + 1

