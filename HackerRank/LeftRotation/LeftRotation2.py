import collections
def rotLeft(a: list[int], d: int) -> list[int]:
  a = collections.deque(a)
  a.rotate(-d)
  return list(a)