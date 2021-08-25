from xml.etree import ElementTree

from io import TextIOWrapper


def get_currency_value(xml):
    if isinstance(xml, str):
        try:
            return ElementTree.fromstring(xml).find("Valute[@ID='R01235']").find('Value').text
        except Exception as e:
            return e.__repr__()
    elif isinstance(xml, TextIOWrapper):
        try:
            return ElementTree.parse(xml).getroot().find("Valute[@ID='R01235']").find('Value').text
        except Exception as e:
            return e.__repr__()
    elif isinstance(xml, bytes):
        try:
            return ElementTree.parse(xml).getroot().find("Valute[@ID='R01235']").find('Value').text
        except Exception as e:
            return e.__repr__()
    else:
        raise Exception('Not supported var type')
