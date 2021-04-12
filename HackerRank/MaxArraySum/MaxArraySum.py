def maxSubsetSum(arr: list) -> int:
  dp = dict()
  dp[0], dp[1] = max(0, arr[0]), max(0, arr[0], arr[1])
  for i, num in enumerate(arr[2:], start=2):
    dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2])
  return dp[len(arr)-1]