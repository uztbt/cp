def minimumAbsoluteDifference(arr: list[int]):
  arr.sort()
  ans = 2 * 10 ^ 9
  for i in range(len(arr) - 1):
    v = abs(arr[i + 1] - arr[i])
    if v < ans:
      ans = v
  return ans
