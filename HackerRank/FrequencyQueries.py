from typing import List
from collections import Counter, defaultdict


def freqQuery(q: List[List[int]]):
    counter = Counter()
    reverseDict = defaultdict(list)

    ans = []
    for op, data in q:
        if op == 1:
            counter[data] += 1
            dataNum = counter[data]
            reverseDict[dataNum].append(data)
            if dataNum >= 2:
                reverseDict[dataNum - 1].remove(data)
        elif op == 2:
            if counter[data] > 0:
                counter[data] -= 1
                reverseDict[counter[data]].append(data)
                reverseDict[counter[data] + 1].remove(data)
        else:
            if reverseDict[data] != []:
                ans.append(1)
            else:
                ans.append(0)
    return ans


if __name__ == "__main__":
    q = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
    ans = freqQuery(q)
    print(ans)
