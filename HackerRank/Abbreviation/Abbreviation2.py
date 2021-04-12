def abbreviation(a: str, b: str) -> str:
  dfs = [(len(a) - 1, len(b) - 1)]
  dp = set()
  while len(dfs) > 0:
    pa, pb = dfs.pop()
    if (pa, pb) in dp:
      # (pa, pb) has already tested false
      continue
    dp.add((pa, pb))
    if pb < 0:
      if pa < 0 or a[:pa+1].islower():
        # e.g. a[:pa+1] is either of the form
        # "" or "xyz"
        return "YES"
      else:
        # e.g. a[:pa+1] is of form "xYz"
        continue
    if pa < 0:
      # a is empty while b has some characters
      continue
    if a[pa].isupper():
      if a[pa] == b[pb]:
        # e.g. a[pa] == 'F' and b[pb] = 'F'
        dfs.append((pa-1, pb-1))
      else:
        # e.g. a[pa] == 'F' and b[pb] = 'G'
        continue
    else:
      if a[pa].upper() == b[pb]:
        # e.g. a[pa] == 'f' and b[pb] = 'F'
        dfs.extend([(pa-1, pb-1), (pa-1, pb)])
      else:
        # e.g. a[pa] == 'f' and b[pb] = 'G'
        dfs.append((pa-1, pb))
  return "NO"