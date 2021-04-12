from collections import deque

def _merge(arr: list, lo: int, mid: int, hi: int) -> int:
  former = deque(arr[lo:mid])
  latter = deque(arr[mid:hi])
  acc = 0

  for i in range(hi-lo):
    if len(former) == 0:
      arr[lo+i] = latter.popleft()
      continue
    elif len(latter) == 0:
      arr[lo+i] = former.popleft()
      continue
    f = former[0]
    l = latter[0]
    if l < f:
      acc += len(former)
      arr[lo+i] = latter.popleft()
    else:
      arr[lo+i] = former.popleft()
  
  return acc

def _countInversions(arr: list, lo: int, hi: int) -> int:
  if 2 < hi - lo:
    mid = (lo + hi) // 2
    a = _countInversions(arr, lo, mid)
    b = _countInversions(arr, mid, hi)
    c = _merge(arr, lo, mid, hi)
    return a + b + c
  else:
    return 0

def countInversions(arr: list) -> int:
  l = len(arr)
  if l <= 1:
    return 0
  else:
    return _countInversions(arr, 0, l)