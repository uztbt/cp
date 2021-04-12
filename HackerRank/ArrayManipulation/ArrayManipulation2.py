def arrayManipulation(n: int, queries: list) -> int:
  # arr holds a number in each slot, which represents a difference from the previous value
  arr = [0] * n
  for query in queries:
    a, b, k = query
    arr[a-1] += k # Need to remove the offset
    if b < n:
      # unless the range of the effect lasts to the last element
      arr[b] -= k # minus the number at the outer edge of the range
  maxVal = 0
  currentVal = 0
  for v in arr:
    currentVal += v
    if currentVal > maxVal:
      maxVal = currentVal
  return maxVal