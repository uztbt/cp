from calendar import month_abbr
from datetime import datetime, timedelta, tzinfo

month_abbrToNaturalNumber = {v: k for k, v in enumerate(month_abbr)}


def toDatetime(t: str):
    # Split into elements
    # Sun 10 May 2015 13:54:36 -0700
    # => ["Sun", "10", "May", "2015", "13:54:36", "-0700"]
    lst = t.split()

    time = lst[4].split(sep=":")
    offset = lst[-1]

    class TZ(tzinfo):
        def utcoffset(self, dt):
            hours = int(offset[:-2])
            if hours >= 0:
                minutes = int(offset[-2:])
            else:
                minutes = -int(offset[-2:])
            return timedelta(hours=hours, minutes=minutes)

    return datetime(
        year=int(lst[3]),
        month=month_abbrToNaturalNumber[lst[2]],
        day=int(lst[1]),
        hour=int(time[0]),
        minute=int(time[1]),
        second=int(time[2]),
        tzinfo=TZ(),
    )


def time_delta(t1: str, t2: str):
    t1_dt, t2_dt = toDatetime(t1), toDatetime(t2)
    return abs(int((t1_dt - t2_dt).total_seconds())).__str__()


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        t1, t2 = input(), input()
        td = time_delta(t1, t2)
        print(td)
