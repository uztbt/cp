def largestRectangle(h: list):
  stack = [(0, 0)]
  h.append(0)
  largest = 0
  for i, height in enumerate(h, 1):
    tallest = stack[-1]
    leftWall = i
    while tallest[0] > height:
      largest = max(
        largest,
        tallest[0] * (i - tallest[1])
      )
      stack.pop()
      leftWall = tallest[1]
      tallest = stack[-1]
    if tallest[0] == height:
      pass
    else:
      # tallest[0] < height
      stack.append((height, leftWall))
  return largest