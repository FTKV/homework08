from collections import defaultdict
from datetime import datetime, timedelta

from users import USERS, DATE_FORMAT


def get_birthdays_per_week(users):
    current_date = datetime.now().date()
    next_monday_date = current_date + timedelta(days=7-current_date.weekday())
    result = defaultdict(list)
    is_leap_year_flag = is_leap_year(next_monday_date.year)
    for user in users:
        date_of_birth = datetime.strptime(user["birthday"], DATE_FORMAT)
        if not is_leap_year_flag and date_of_birth.month == 2 and date_of_birth.day == 29:
            date_delta = datetime(year=next_monday_date.year, month=3, day=1).date() - next_monday_date
        else:
            date_delta = datetime(year=next_monday_date.year, month=date_of_birth.month, day=date_of_birth.day).date() - next_monday_date
        delta_days = date_delta.days
        if delta_days > 360:
            delta_days -= 365 + is_leap_year_flag
        elif delta_days < -360:
            delta_days += 365 + is_leap_year_flag
        if delta_days >= -2 and delta_days <=4:
            if delta_days < 0:
                delta_days = 0
            result[delta_days].append(user["name"])
    
    for i in range(0, 5):
        if result[i]:
            weekday = (next_monday_date + timedelta(days=i)).strftime("%A")
            names = ", ".join(result[i])
            print(f"{weekday}: {names}")


def is_leap_year(year):
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False

get_birthdays_per_week(USERS)