def twoStrings(s1: str, s2: str) -> str:
  if frozenset(s1).isdisjoint(s2):
    return "NO"
  else:
    return "YES"