def countingValleys(steps: int, path: str) -> int:
  acc = 0
  altitude: int = 0
  for step in path:
    if step == 'U':
      altitude += 1
    else:
      altitude -= 1
    if altitude == 0 and step == 'U':
      acc += 1
  return acc