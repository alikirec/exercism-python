from datetime import datetime, timedelta

TIME_DELTA_SECONDS = 10 ** 9


def add(moment: datetime):
    """
    Given a moment, returns that would be after a gigasecond has passed
    """
    return moment + timedelta(seconds=TIME_DELTA_SECONDS)
