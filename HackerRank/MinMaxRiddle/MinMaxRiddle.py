from collections import deque

def riddle(arr: list):
  n = len(arr)
  maxMins = [max(arr)]
  prevWindows = arr
  for _ in range(2, n+1):
    pair = deque([10 ** 9, prevWindows[0]], 2)
    currentWindows = []
    for item in prevWindows[1:]:
      pair.append(item)
      currentWindows.append(min(pair))
    maxMins.append(max(currentWindows))
    prevWindows = currentWindows
  return maxMins