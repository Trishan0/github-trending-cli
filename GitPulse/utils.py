from datetime import date, timedelta

today = date.today()
first_this_month = today.replace(day=1)

start_of_this_week = today - timedelta(days=today.weekday())
start_of_last_week = start_of_this_week - timedelta(days=7)
end_of_last_week = start_of_this_week - timedelta(days=1)


def get_last_x_days(x: int) -> date:
    target_date = today - timedelta(days=x)
    return f">{target_date}"


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


def get_date_ranges(duration: str, calendar_mode: bool = False) -> str:
    """
    Get date range string for GitHub API based on duration.

    Args:
        duration: 'day', 'week', 'month', or 'year'
        calendar_mode: If True, use calendar-based ranges (prev week/month/year)
                      If False, use rolling ranges (last X days)

    Returns:
        Date range string for GitHub API query
    """

    if calendar_mode:
        if duration == "week":
            return get_previous_week_range()
        elif duration == "month":
            return get_last_month_range()
        elif duration == "year":
            return get_last_year_range()
        elif duration == "day":
            return get_last_x_days(1)

    else:
        days_map = {"day": 1, "week": 7, "month": 30, "year": 365}
        return get_last_x_days(days_map.get(duration, 1))

    return get_last_x_days(7)
