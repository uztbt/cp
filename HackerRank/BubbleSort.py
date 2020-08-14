#!/bin/python3
import array


def bubbleSort(arr):
    arrLen = len(arr)
    swapNum = 0
    for i in range(arrLen):
        for j in range(arrLen - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                swapNum += 1
    return (swapNum, arr[0], arr[arrLen - 1])


if __name__ == "__main__":
    n = int(input())
    mp = map(int, input().split())
    swapNum, first, last = bubbleSort(array.array("i", mp))
    print("Array is sorted in {0} swaps.".format(swapNum))
    print("First Element: {0}".format(first))
    print("Last Element: {0}".format(last))
