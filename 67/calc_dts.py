from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date(start=start_100days):
    """Return a string of yyyy-mm-dd"""
    start += + timedelta(days=100)
    return start.strftime("%Y-%m-%d")


def get_days_between_pb_start_first_joint_pycon(start=pybites_founded, end=pycon_date):
    """Return the int number of days"""
    difference = end - start
    return difference.days