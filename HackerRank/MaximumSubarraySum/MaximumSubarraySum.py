import bisect

def maximumSum(arr: list, m: int) -> int:
  prefix = [0]
  curr = 0
  maximum = 0
  for item in arr:
    curr = (curr + item) % m
    want = (curr - (m - 1)) % m # from `curr - want = m - 1`
    # Consider a situation where `m = 5 and curr = 2` ==> `want = 2`
    # case 1 `prefix = [0, 1]`: then `l = 2`
    # case 2 `prefix = [0, 3]`: then `l = 1`
    l = bisect.bisect_left(prefix, want) 
    if l == len(prefix):
      # case 1.
      maximum = max(maximum, curr)
    else:
      # case 2.
      maximum = max(maximum, (curr - prefix[l]) % m)

    currIndex = bisect.bisect_left(prefix, curr)
    if currIndex < len(prefix) and prefix[currIndex] == curr:
      pass
    else:
      bisect.insort(prefix, curr)
  return maximum