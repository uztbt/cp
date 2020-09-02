from typing import List


def luckBalance(k: int, contests: List[List[int]]):
    res = 0
    for contest in sorted(contests, key=lambda c: c[0], reverse=True):
        li, ti = contest
        if ti == 0:
            res += li
        elif k > 0:
            res += li
            k -= 1
        else:
            res -= li
    return res
