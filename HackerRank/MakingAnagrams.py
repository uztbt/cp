ordA = ord("a")


def toIndex(x):
    return ord(x) - ordA


def makeAnagram(a, b):
    signatureA = [0] * 26
    signatureB = [0] * 26
    for ax in a:
        signatureA[toIndex(ax)] += 1
    for bx in b:
        signatureB[toIndex(bx)] += 1
    acc = 0
    for i in range(len(signatureA)):
        acc += abs(signatureA[i] - signatureB[i])
    return acc
