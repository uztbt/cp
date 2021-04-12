#!/bin/python3

from typing import List


def leftRotation(a: List[int], d: int):
    moving = a[:d]
    return a[d:] + moving


if __name__ == "__main__":
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    ans = leftRotation(a, d)
    for i in range(n):
        print(ans[i], end=" ")
