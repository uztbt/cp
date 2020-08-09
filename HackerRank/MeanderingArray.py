from typing import List


def meanderingArray(unsorted):
    length = len(unsorted)
    half = len(unsorted) // 2
    unsorted.sort()  # sorted
    meandering = []
    for i in range(half):
        meandering += [
            unsorted[-i - 1],
            unsorted[i],
        ]
    if length % 2 == 1:
        meandering.append(unsorted[half])
    return meandering


#
# n = 8
# unsorted = [7, 5, 2, 7, 8, -2. 25. 25]
# answer = [25, -2, 25, 2, 8, 5, 7, 7]
# sorted =[-2, 2, 5, 7, 7, 8, 25, 25]

# i = 0: [25, -2]
# i = 1: [25, -2, 25, 2]
# i = 2: [25, -2, 25, 2, 8, 5]
# i = 3: [25, -2, 25, 2, 8, 5, 7, 7]
#
# #
