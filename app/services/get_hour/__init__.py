from re import search
def get_hour(date: str):
    regex_date = search(r'[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}', date)
    time = date[regex_date.span()[0]:regex_date.span()[1]]

    return int(time[0:2])
