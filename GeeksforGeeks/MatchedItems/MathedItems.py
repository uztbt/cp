def findMatchedItems(strings: list[list[str]], target: list[str]) -> list[int]:
  acc = []
  for i, string in enumerate(strings[:len(strings)-len(target)+1]):
    match = True
    for j in range(target):
      if string[i+j] != target[j]:
        match = False
        break
    if match:
      acc.append(i)
  return acc