def commonChild(s1: str, s2: str) -> int:
  n = len(s1)
  # (lastIndexOfS1, lengthOfTheCommonChild)
  table: list[list[tuple]] = [[(0, 0) for _ in range(n+1)] for _ in range(n+1)]

  for i, c1 in enumerate(s1, start=1):
    for j, c2 in enumerate(s2, start=1):
      if c1 != c2 or table[i][j-1][0] == i:
        table[i][j] = better(table[i][j-1], table[i-1][j])
      else: # c1 == c2 and table[i][j-1][0] < i
        cand = (i, table[i][j-1][1]+1)
        table[i][j] = better(cand, table[i-1][j])

  return table[n][n][1]

def better(v1: tuple, v2: tuple) -> tuple:
  l1, l2 = v1[1], v2[1]
  if l1 < l2:
    return v2
  elif l1 > l2:
    return v1
  else:
    # If both strings are as long as each other,
    # prefer the one whose last index in s1 is smaller
    if v1[0] < v2[0]:
      return v1
    else:
      return v2