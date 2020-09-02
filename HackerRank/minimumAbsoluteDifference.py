from typing import List


def minimumAbsoluteDifference(arr: List[int]):
    arr.sort()
    mad: int = 2 * 10 ** 9
    for i in range(len(arr) - 1):
        if abs(arr[i + 1] - arr[i]) < mad:
            mad = abs(arr[i + 1] - arr[i])
    return mad
