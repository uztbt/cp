def abbreviation(a:str, b:str) -> str:
  dfs = [(len(a)-1, len(b)-1)]
  dp = set()
  while len(dfs) > 0:
    pa, pb = dfs.pop()
    if (pa, pb) in dp:
      # (pa, pb) has been already visited in vain
      continue
    dp.add((pa, pb))
    if pb < 0:
      if pa < 0 or a[:pa+1].islower():
        # e.g. a is of form either
        # "" or "xyz"
        return "YES"
      else:
        # e.g. a is of form "xYz"
        continue
    if pa < 0:
      # a is empty while b has some characters
      continue
    if a[pa].isupper():
      if a[pa] == b[pb]:
        # e.g. a[pa] = 'F' and b[pb] = 'F'
        dfs.append((pa-1, pb-1))
      else:
        # e.g. a[pa] = 'D' and b[pb] = 'F'
        continue
    else:
      if a[pa].capitalize() == b[pb]:
        # e.g. a[pa] = "f" and b[pb] = 'F'
        dfs.append((pa-1, pb)) # skip on a
        dfs.append((pa-1, pb-1)) # delete both
      else:
        # e.g. a[pa] = 'c' and b[pb] = 'F'
        dfs.append((pa-1, pb))
  return "NO"