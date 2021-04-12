if __name__ == "__main__":
    s = input()

    alphabet = list(map(chr, range(ord("a"), ord("z") + 1)))

    alphaDict = {}

    for c in alphabet:
        alphaDict[c] = 0

    for c in s:
        alphaDict[c] += 1

    alphaPairs = []

    for c in alphabet:
        alphaPairs.append((c, alphaDict[c]))

    ordz = ord("z")
    orderedAlphaPairs = sorted(
        alphaPairs, key=lambda kv: (kv[1], ordz - ord(kv[0])), reverse=True
    )

    for i in range(3):
        pair = orderedAlphaPairs[i]
        print(pair[0], pair[1])
