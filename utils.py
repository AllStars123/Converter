def is_float(string: str):
    try:
        float(string.replace(',', '.'))
        return True
    except ValueError:
        return False


def is_int(string: str):
    try:
        int(string)
        return True
    except ValueError:
        return False
