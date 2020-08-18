from typing import List, Tuple


def countConsecutives(n, s, prevSSs: List[Tuple[int, int]], prevLen, total, duplicates):
    currentSSs: List[(int, int)] = []
    for fst, snd in prevSSs:
        if snd < n - 1:
            if s[snd + 1] == s[snd]:
                currentSSs.append((fst, snd + 1))
    total += len(prevSSs)
    if prevLen % 2 == 1:
        duplicates += len(prevSSs)
    if currentSSs == []:
        return total, duplicates
    else:
        return countConsecutives(n, s, currentSSs, prevLen + 1, total, duplicates)


def secondTypes(n, s, prevSSs, prevLen, total):
    currentSSs: List[(int, int)] = []
    for ss in prevSSs:
        if ss[0] > 0 and ss[1] < n - 1:
            formerCharIndex = ss[0] - 1
            latterCharIndex = ss[1] + 1
            if s[formerCharIndex] == s[latterCharIndex]:
                if prevLen == 1 or s[formerCharIndex] == s[ss[0]]:
                    currentSSs.append((formerCharIndex, latterCharIndex))
    total += len(prevSSs)
    if currentSSs == []:
        return total
    else:
        return secondTypes(n, s, currentSSs, prevLen + 2, total)


def substrCount(n, s: str):
    prevSSs: List[(int, int)] = []
    for index in range(len(s)):
        prevSSs.append((index, index))
    firstTotal, duplicates = countConsecutives(n, s, prevSSs, 1, 0, 0)
    secondTotal = secondTypes(n, s, prevSSs, 1, 0)
    return firstTotal + secondTotal - duplicates


if __name__ == "__main__":
    print(substrCount(4, "aaaa"))
