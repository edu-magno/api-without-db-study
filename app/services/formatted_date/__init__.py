from re import search

def formatted_date(date: str) -> str:

    splited_date = date.split(' ')

    regex_date = search(r'[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}', date)
    date_formatted = []
    for arg in splited_date:
        regex_date = search(r'[0-9]{2}[:]{1}[0-9]{2}[:]{1}[0-9]{2}', arg)
        if regex_date != None:
            arg = f'{arg[0:2]}:00:00'
            date_formatted.append(arg)
            continue

        date_formatted.append(arg)

    return ' '.join(date_formatted)