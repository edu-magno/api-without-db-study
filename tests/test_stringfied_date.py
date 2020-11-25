from app.services.stringfied_date import stringfied_date

def test_stringfied_date():
    result = stringfied_date(10,12,2020)
    expected = 'Thu Dec 10 2020'

    assert expected == result

def test_stringfied_date_2():
    result = stringfied_date(25,11,2020)
    expected = 'Wed Nov 25 2020'

    assert expected == result
