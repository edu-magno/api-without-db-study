from app.services.get_hour import get_hour


def test_get_hour():
    result = get_hour("Wed Sep 09 2020 07:52:13 GMT-0300 (-03)")
    expected = 7

    assert expected == result


def test_get_hour_2():
    result = get_hour("Wed Sep 09 2020 16:52:13 GMT-0300 (-03)")
    expected = 16

    assert expected == result
