from datetime import datetime


def toDatetime(t: str):
    # t= "Sun 10 May 2015 13:54:36 -0700"
    dt = datetime.strptime(t, "%a %d %b %Y %H:%M:%S %z")
    return dt


def time_delta(t1: str, t2: str):
    t1_dt, t2_dt = toDatetime(t1), toDatetime(t2)
    return int((t1_dt - t2_dt).total_seconds()).__str__()


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        t1, t2 = input(), input()
        td = time_delta(t1, t2)
        print(td)
