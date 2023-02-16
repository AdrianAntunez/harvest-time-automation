from datetime import date


def currentday():
    return date.today()


def isweekday(set_day):
    if set_day.weekday() < 5:
        return True
    else:
        return False
