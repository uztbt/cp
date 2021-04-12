#!/bin/python3

from typing import List


def hourglass(a: List[List[int]], r: int, c: int):
    return (
        a[r][c]
        + a[r][c + 1]
        + a[r][c + 2]
        + a[r + 1][c + 1]
        + a[r + 2][c]
        + a[r + 2][c + 1]
        + a[r + 2][c + 2]
    )


def hourglassSum(arr: List[List[int]]):
    max = -63
    for i in range(4):
        for j in range(4):
            current = hourglass(arr, i, j)
            if current > max:
                max = current
    return max


if __name__ == "__main__":
    arr = []
    for i in range(6):
        l = input()
        arr.append(list(map(int, l.split())))
    print(hourglassSum(arr))
