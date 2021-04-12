def update(l: int, s: int, p: int, n: int, candies:int) -> set:
  # produce
  candies += l*s
  noInvestmentTpl = (l, s, p, n,candies)
  ret = set()
  ret.add(noInvestmentTpl)
  if s*s >= n or candies >= n:
    # Case 1: No need to invest
    return ret
  # Investments to make
  investments, candies = divmod(candies, p)
  if l >= s + investments:
    # Invest all in s
    investAllInSTpl = (l, s + investments, p, n, candies)
    ret.add(investAllInSTpl)
    return ret
  else:
    # Invest in s till it becomes equal to l
    investments -= l - s
    s = l
    even, odd = divmod(investments, 2)
    l += even + odd
    s += even
    investEvenlyTpl = (l, s, p, n, candies)
    ret.add(investEvenlyTpl)
    return ret

def minimumPasses(m: int, w: int, p: int, n: int) -> int:
  wfs = set()
  # l, s, p, n, candy
  wfs.add((
    max(m, w),
    min(m, w),
    p,
    n,
    0
  ))

  for i in range(1, n):
    # From day 1 to day n, which is the loose upper bound
    copy = wfs.copy()
    wfs = set()
    for tpl in copy:
      updatedDct = update(*tpl)
      wfs = wfs.union(updatedDct)
    for tpl in wfs:
      if tpl[4] >= n:
        return i