def maxHourglass(a: list) -> int:
  maxVal = -63 # the minimum hourglass sum is 7 * (-9) = -63
  for row in range(len(a) - 2):
    # This code block is executed when len(a) >= 3
    for col in range(len(a[0]) - 2):
      # This code block is executed when len(a[0]) >= 3
      v = a[row][col] + a[row][col+1] + a[row][col+2] + a[row+1][col+1] + a[row+2][col] + a[row+2][col+1] + a[row+2][col+2]
      if v > maxVal:
        maxVal = v
  return maxVal