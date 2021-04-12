from typing import List
from collections import deque


def maxMin(k: int, arr: List[int]):
    arr.sort()
    dq = deque(arr[:k], maxlen=k)
    res = dq[-1] - dq[0]
    for i in range(k, len(arr)):
        dq.append(arr[i])
        current = dq[-1] - dq[0]
        if current < res:
            res = current
    return res


if __name__ == "__main__":
    print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30]))

