from datetime import datetime

def stringfied_date(day,month,year):
     date = datetime(year, month, day).strftime('%a %b %d %Y')
     return date