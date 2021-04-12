def repeatedString(s: str, n: int):
  (q, r) = divmod(n, len(s))
  return s.count('a') * q + s[:r].count('a')
