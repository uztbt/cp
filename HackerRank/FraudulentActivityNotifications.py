#!/bin/python3
from typing import List
from collections import deque


def findPlace(arr, length, i):
    # i is greater than or equal to arr[j]

    for j in range(length):
        if arr[j] >= i:
            return j
    return length


def median(reverseTrailing, d):
    target = d // 2
    if d % 2 == 1:
        for i in range(200):
            target -= reverseTrailing[i]
            if target < 0:
                return i
    else:
        for i in range(200):
            target -= reverseTrailing[i]
            if target <= 0:
                acc = i
                if target == 0:
                    for j in range(i + 1, 200):
                        if reverseTrailing[j] > 0:
                            acc += j
                            break
                    return acc / 2
                else:
                    return acc


def activityNotifications(expenditure: List[int], d: int):
    trailingExpenditures = expenditure[:d]
    expenditure = expenditure[d:]
    trailingExpenditures = deque(trailingExpenditures, d)
    reverseTrailing = [0] * 201
    for expense in trailingExpenditures:
        reverseTrailing[expense] += 1

    res = 0
    for expense in expenditure:
        if median(reverseTrailing, d) * 2 <= expense:
            res += 1
        oldestInTrailing = trailingExpenditures.popleft()  # O(1)
        trailingExpenditures.append(expense)  # O(1)
        reverseTrailing[oldestInTrailing] -= 1
        reverseTrailing[expense] += 1
    return res


if __name__ == "__main__":
    print(activityNotifications([10, 20, 30, 40, 50], 3))

