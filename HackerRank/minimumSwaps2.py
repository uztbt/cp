#!/bin/python3
from typing import List
import array

# Slow
# def minimumSwaps(arr: List[int]):
#     length = len(arr)
#     swapNum = 0
#     for i in range(length, 1, -1):
#         tail = arr.pop()
#         if tail == i:
#             pass
#         else:
#             index = arr.index(i)
#             arr[index] = tail
#             swapNum += 1
#     return swapNum


# Slow too
# def minimumSwaps(arr: List[int]):
#     length = len(arr)
#     swapNum = 0
#     dictionary = {}
#     for i in range(1, length):
#         resolved = arr[0]
#         tmp = resolved

#         while resolved is not None:
#             tmp = resolved
#             resolved = dictionary.get(tmp)
#         resolved = tmp

#         if resolved == i:
#             pass
#         else:
#             dictionary[i] = resolved
#             swapNum += 1
#         arr = arr[1:]
#     return swapNum


def minimumSwaps(arr: List[int]):
    swapNum = 0

    regularized = map(lambda x: x - 1, arr)
    forward = array.array("i", regularized)
    backward = array.array("i", arr)
    for i, v in enumerate(forward):
        backward[v] = i

    for i, v in enumerate(forward):
        if v == i:
            pass
        else:
            swapNum += 1
            pos_i = backward[i]
            forward[pos_i] = v
            backward[v] = pos_i
    return swapNum


if __name__ == "__main__":
    print(minimumSwaps([4, 3, 1, 2]))

