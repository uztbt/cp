from collections import defaultdict
import bisect


def calcR(s1: str, s2: str):
    s2Dict = defaultdict(list)
    for j in range(len(s2)):
        s2Dict[s2[j]].append(j + 1)  # offset for the LCS
    s2Dict = {k: list(reversed(v)) for k, v in s2Dict.items()}
    r = {}
    for i in range(len(s1)):
        js = s2Dict.get(s1[i])
        if js is None:
            js = []
        r[i + 1] = js  # offset for the LCS
    return r


def commonChild(s1: str, s2: str):
    r = calcR(s1, s2)
    t = [0]
    for i in range(1, len(s1) + 1):
        for j in r[i]:
            index = bisect.bisect_left(t, j)
            if index < len(t):
                t.pop(index)
            t.insert(index, j)
    return len(t) - 1


if __name__ == "__main__":
    s1 = "SHINCHAN"
    s2 = "NOHARAAA"
    print(commonChild(s1, s2))
