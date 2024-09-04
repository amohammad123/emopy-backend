from django.utils import timezone
import jdatetime


def time_now():
    return int(timezone.now().timestamp())


def get_shamsi():
    current_time = time_now()
    shamsi_time = jdatetime.datetime.fromtimestamp(timestamp=current_time)
    result = {
        'year': shamsi_time.year,
        'month': shamsi_time.month,
        'day': shamsi_time.day,
        'time': {
            'hour': shamsi_time.hour,
            'minute': shamsi_time.minute,
            'second': shamsi_time.second
        }
    }
    return result
