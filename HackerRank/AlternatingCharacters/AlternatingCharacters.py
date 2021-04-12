def alternatingCharacters(s):
    deletions = 0
    prev = s[0]
    for current in s[1:]:
        if current == prev:
            deletions += 1
        prev = current
    return deletions
