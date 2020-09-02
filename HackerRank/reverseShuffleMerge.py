from collections import defaultdict
from typing import DefaultDict, List


def createDict(s: str) -> DefaultDict:
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d


def smallestChar(d: DefaultDict, keys: List[str]) -> str:
    for k in keys:
        if d[k] > 0:
            return k
    raise "aa"


def reverseShuffleMerge(s: str) -> str:
    sDict = createDict(s)
    aDict = {k: v // 2 for k, v in sDict.items()}
    zDict = {k: 0 for k in sDict.keys()}
    smallestA = ""
    p = len(s) - 1
    tookAt = len(s)
    keys = sorted(sDict.keys())
    while aDict != zDict:
        pChar = s[p]
        if pChar == smallestChar(aDict, keys):
            smallestA += pChar
            tookAt = p
            aDict[pChar] -= 1
        elif sDict[pChar] > aDict[pChar]:
            # skip
            pass
        else:
            # backtrack
            substring = s[p:tookAt]
            for c in sorted(substring):
                if aDict[c] > 0:
                    pChar = c
                    for i in range(tookAt - 1, p - 1, -1):
                        if s[i] == pChar:
                            p = i
                            break
                    smallestA += pChar
                    tookAt = p
                    aDict[c] -= 1
                    sDict = createDict(s[: tookAt + 1])
                    break
        sDict[pChar] -= 1
        p -= 1
    return smallestA


if __name__ == "__main__":
    result = reverseShuffleMerge(
        "djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida"
    )
    print(result)
