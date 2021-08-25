from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection

from urllib.parse import urlparse, parse_qs

from currency_parser import get_currency_value

from json import dumps

from datetime import datetime

from utils import is_float, is_int


class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        data = parse_qs(urlparse(self.path).query)
        if not data:
            response = dumps({'error_code': 601, 'error_message': 'No data values passed'})
            self.wfile.write(bytes(response, encoding='utf-8'))
            raise Exception('Amount parameter isn`t specified')
        if 'amount' in data.keys() and (is_float(data['amount'][0]) or is_int(data['amount'][0])):
            rate = send_request()
            amount = float(data['amount'][0].replace(',', '.'))
            if 'from' in data.keys() and 'to' in data.keys():
                from_ = data['from'][0]
                to_ = data['to'][0]
                if from_ in ['usd', 'rub'] and to_ in ['usd', 'rub']:
                    if from_ == to_:
                        result = amount
                    else:
                        if from_ == 'usd':
                            result = rate * amount
                        else:
                            result = amount / rate
                else:
                    response = dumps({'error_code': 602, 'error_message': 'Unsupported currency'})
                    self.wfile.write(bytes(response, encoding='utf-8'))
                    raise Exception('Unsupported currency!')
            elif 'from' not in data.keys() and 'to' not in data.keys():
                result = amount / rate
                from_ = 'rub'
                to_ = 'usd'
            else:
                response = dumps({'error_code': 603, 'error_message': 'Incorrect parameters passed'})
                self.wfile.write(bytes(response, encoding='utf-8'))
                raise Exception('Please, specify both from and to params')
            json_data = dumps({'from_currency': from_, 'to_currency': to_, 'amount': amount, 'result': result, 'rate': rate})
            self.wfile.write(bytes(json_data, encoding='utf-8'))
            return
        response = dumps({'error_code': 604, 'error_message': 'Amount parameter isn`t specified'})
        self.wfile.write(bytes(response, encoding='utf-8'))
        raise Exception('Amount parameter isn`t specified')


def send_request():
    now = datetime.now().strftime('%d/%m/%Y')
    conn = HTTPConnection('www.cbr.ru', 80)
    conn.request('GET', '/scripts/XML_daily.asp?date_req=' + now)
    resp = conn.getresponse()
    currency = get_currency_value(resp.read().decode('windows-1251')).replace(',', '.')
    conn.close()
    return float(currency)

