#!/bin/python3

from typing import List


def minimumBribes(q: List[int]):
    length = len(q)
    bribe = 0
    q.reverse()
    for k in range(length, 0, -1):
        if q[0] == k:
            b = 0
        elif q[1] == k:
            b = 1
        elif q[2] == k:
            b = 2
        else:
            return -1
        q.pop(b)
        bribe += b
    return bribe


if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        q = list(map(int, input().split()))
        b = minimumBribes(q)
        if b == -1:
            print("Too chaotic")
        else:
            print(b)
