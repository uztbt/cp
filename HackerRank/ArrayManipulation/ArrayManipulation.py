#!/bin/python3

from typing import List
import array


def arrayManipulation(n: int, queries: List[List[int]]):
    arr = array.array("i", [0] * (n + 1))
    for a, b, k in queries:
        arr[a - 1] += k
        arr[b] -= k

    maximum = 0
    acc = 0
    for v in arr:
        acc += v
        if acc > maximum:
            maximum = acc
    return maximum


if __name__ == "__main__":
    arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])

