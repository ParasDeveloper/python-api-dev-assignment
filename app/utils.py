from datetime import datetime
from sqlalchemy import inspect

def correct_date_format(date_str):
    """Correct the date format from 'YY.DD.MM' to 'YYYY-MM-DD'"""
    return datetime.strptime(date_str, '%y.%d.%m')


def check_if_column_exists(model, attribute):
    mapper = inspect(model)
    if attribute in mapper.attrs:
        return True
    else:
        return False