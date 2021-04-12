def alternatingCharacters(s: str) -> int:
  deletionNum = 0
  stringOf = s[0]
  for c in s[1:]:
    if c != stringOf:
      # i.e. AB or BA
      stringOf = c
    else:
      # i.e. AA or BB
      deletionNum += 1
  return deletionNum