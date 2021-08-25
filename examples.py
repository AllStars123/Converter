from requests import get


# Доллар -> рубли
# amount - количество валюты
def get_data_amount(amount):
    return eval(get('http://localhost', params={'amount': amount}).text)


# from_ - Из какой валюты
# to_ - В какую валюту
# amount - Количество валюты
# Можно переводить из долларов в рубли,наоборот, рубли в рубли и доллары в доллары
# amount - может быть и float, и int
# amount может быть передано и строкой
# а также со знаком ","
def get_data_amount_params(amount, from_, to_):
    return eval(get('http://localhost', params={'amount': amount, 'from': from_, 'to': to_}).text)


print(get_data_amount(1153.5654))
print(get_data_amount_params(15.6, 'usd', 'rub'))
