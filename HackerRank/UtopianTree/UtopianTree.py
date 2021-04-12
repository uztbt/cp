def utopianTree(n: int) -> int:
  (q, r) = divmod(n, 2)
  if r == 1:
    return 2 * (2 ** (q+1) - 1)
  else:
    return 2 ** (q+1) - 1


