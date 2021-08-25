from requests import get, post

""" Может быть использовано только в связке с main.py запущенным паралельно """

"""
Ошибки

601 - Параметры не переданы или переданы неверно
602 - Неверная валюта
603 - Переданы неверные параметры
604 - Не указано количество валюты

Ошибки
"""


def get_empty_data():
    return eval(get('http://localhost', params={}).text)


def get_invalid_data():
    return eval(get('http://localhost', params={'invalid': 'data'}).text)


def get_without_amount_specified():
    return eval(get('http://localhost', params={'from': 'usd'}).text)


def get_not_enough_params_from():
    return eval(get('http://localhost', params={'amount': 800, 'from': 'usd'}).text)


def get_not_enough_params_to():
    return eval(get('http://localhost', params={'amount': 400, 'to': 'usd'}).text)


def get_invalid_currency_from():
    return eval(get('http://localhost', params={'amount': 800, 'from': 'yun', 'to': 'usd'}).text)


def get_invalid_currency_to():
    return eval(get('http://localhost', params={'amount': 800, 'from': 'usd', 'to': 'ten'}).text)


def get_invalid_currency_both():
    return eval(get('http://localhost', params={'amount': 800, 'from': 'rng', 'to': 'tbh'}).text)


def get_invalid_float_string():
    return eval(get('http://localhost', params={'amount': '152,743459375', 'from': 'rub', 'to': 'usd'}).text)


def get_from_rub_to_usd():
    return eval(get('http://localhost', params={'amount': '5648.59375', 'from': 'rub', 'to': 'usd'}).text)


def get_from_usd_to_usd():
    return eval(get('http://localhost', params={'amount': '5648.59375', 'from': 'usd', 'to': 'usd'}).text)


def get_from_rub_to_rub():
    return eval(get('http://localhost', params={'amount': '5648.59375', 'from': 'rub', 'to': 'rub'}).text)


def get_from_usd_to_rub():
    return eval(get('http://localhost', params={'amount': '5648.59375', 'from': 'usd', 'to': 'rub'}).text)


def get_from_usd_to_rub_no_params():
    return eval(get('http://localhost', params={'amount': '5648.59375'}).text)


def test_empty_data():
    assert get_empty_data()['error_code'] == 601


def test_invalid_data():
    assert get_invalid_data()['error_code'] == 604


def test_without_amount_specified():
    assert get_without_amount_specified()['error_code'] == 604


def test_not_enough_params_from():
    assert get_not_enough_params_from()['error_code'] == 603


def test_not_enough_params_to():
    assert get_not_enough_params_to()['error_code'] == 603


def test_invalid_currency_from():
    assert get_invalid_currency_from()['error_code'] == 602


def test_invalid_currency_to():
    assert get_invalid_currency_to()['error_code'] == 602


def test_invalid_currency_both():
    assert get_invalid_currency_both()['error_code'] == 602


def test_invalid_float_string():
    assert 'error_code' not in get_invalid_float_string().keys()


def test_from_rub_to_usd():
    assert 'amount' in get_from_rub_to_usd().keys()


def test_from_usd_to_rub():
    assert 'amount' in get_from_usd_to_rub().keys()


def test_from_usd_to_usd():
    assert 'amount' in get_from_usd_to_usd().keys()


def test_from_rub_to_rub():
    assert 'amount' in get_from_rub_to_rub().keys()


def test_from_usd_to_rub_no_params():
    assert 'amount' in get_from_usd_to_rub_no_params().keys()


if __name__ == '__main__':

    test_empty_data() # Пустой GET
    test_invalid_data() # Невалидные параметры
    test_without_amount_specified() # Не передано количество валюты
    test_not_enough_params_from() # Параметр from без to
    test_not_enough_params_to() # Параметр to без from
    test_invalid_currency_from() # Параметр from некорректен
    test_invalid_currency_to() # Параметр to некорректен
    test_invalid_currency_both() # Оба параметра from и to некорректны
    test_invalid_float_string() # Передано количество валюты в формате x,yz
    test_from_rub_to_usd() # Рубли в доллары
    test_from_usd_to_rub() # Доллары в рубли
    test_from_usd_to_usd() # Доллары в доллары
    test_from_rub_to_rub() # Рубли в рубли
    test_from_usd_to_rub_no_params() # Доллары в рубли без переданных параметров from и to
    print(get_not_enough_params_from)
