from csv import DictWriter
def clean_up_file(file_path, fieldnames):
    with open(file_path, 'w' ) as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()