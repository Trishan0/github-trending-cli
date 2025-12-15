from datetime import date, timedelta

today = date.today()
first_this_month = today.replace(day=1)

start_of_this_week = today - timedelta(days=today.weekday())
start_of_last_week = start_of_this_week - timedelta(days=7)
end_of_last_week = start_of_this_week - timedelta(days=1)

def get_last_x_days(x:int)->date:
    return today - timedelta(days=x)

def get_previous_week_range():
    query_param = f"{start_of_last_week}..{end_of_last_week}"
    return query_param

def get_last_month_range():
    last_day_last_month = first_this_month - timedelta(days=1)
    first_day_last_month = last_day_last_month.replace(day=1)
    query_param = f"{first_day_last_month}..{last_day_last_month}"
    return query_param

def get_last_year_range():
    last_year = today.year - 1 
    start_last_year = date(last_year, 1, 1)
    end_last_year = date(last_year, 12, 31)
    query_param = f"{start_last_year}..{end_last_year}"
    return query_param
    