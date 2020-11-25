from app.services.formatted_date import formatted_date

def test_formatted_date():
    result = formatted_date("Tue Sep 09 2020 10:52:13 GMT-0300 (-03)")
    expected = "Tue Sep 09 2020 10:00:00 GMT-0300 (-03)"

    assert expected == result

def test_formatted_date_2():
    result = formatted_date("Tue Sep 09 2020 11:11:00 GMT-0300 (-03)")
    expected = "Tue Sep 09 2020 11:00:00 GMT-0300 (-03)"

    assert expected == result