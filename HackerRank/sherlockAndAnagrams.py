import array
from collections import Counter

# alphabet = array.array("i", range(ord("a"), ord("z") + 1))
emptySignature = [0] * 26


def toSignature(arr: array.array):
    signature = emptySignature.copy()
    for k in arr:
        signature[k] += 1
    return tuple(signature)


def sherlockAndAnagrams(s: str):
    arrayS = array.array("i", map(lambda c: ord(c) - ord("a"), s))
    length = len(s)
    signatures = Counter()
    for chunkLength in range(1, length):
        for start in range(0, length - chunkLength + 1):  # len(s) = 2, chunkLength = 1
            signatures[toSignature(arrayS[start : start + chunkLength])] += 1
    print(signatures)
    res = 0
    for count in signatures.values():
        res += count * (count - 1) // 2
    return res


# My original answer
def sherlockAndAnagramsOrig(s: str):
    counter = Counter()
    lst = map(ord, s)
    arr = array.array("i", lst)
    length = len(arr)
    for chunkLength in range(1, length):
        for start in range(
            length - chunkLength + 1
        ):  # Think. length = 2, chunkLength = 1
            subs = sorted(arr[start : start + chunkLength])
            counter[subs.__str__()] += 1

    acc = 0
    for subs in counter:
        # nC2
        n = counter[subs]
        acc += n * (n - 1) // 2
    return acc


if __name__ == "__main__":
    print(sherlockAndAnagrams("abba"))
