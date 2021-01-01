import pytz
from datetime import datetime

from taskler.config import Config


def local_to_utc(local_time):
    """
    Receive local date and convert to UTC with no TZ info
    """
    if not local_time:
        return None
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time.replace(tzinfo=None)
