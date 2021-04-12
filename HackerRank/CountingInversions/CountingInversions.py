def swap(a, b):
    c = []
    swaps = 0
    i, j = 0, 0
    lengthA = len(a)
    lengthB = len(b)
    while i < lengthA and j < lengthB:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j+=1
            swaps += len(a) - i
    if i == lengthA:
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return (c, swaps)


def countInversionsHelper(arr, length):
    if length == 1:
        return (arr, 0)
    formerLength= length//2
    former = arr[:formerLength]
    latter = arr[formerLength:]
    (former,formerSwaps) = countInversionsHelper(former, formerLength)
    (latter, latterSwaps) = countInversionsHelper(latter, length-formerLength)
    (arr, swaps) = swap(former, latter)
    return (arr, formerSwaps + latterSwaps + swaps)

def countInversions(arr):
    (_, swaps) = countInversionsHelper(arr, len(arr))
    return swaps

if __name__ == "__main__":
    arr = []
    print(countInversions(arr))
