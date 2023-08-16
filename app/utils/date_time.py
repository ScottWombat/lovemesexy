
from datetime import datetime, tzinfo
import pytz

  

def get_current_utc_datetime():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")