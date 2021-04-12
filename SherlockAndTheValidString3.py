from collections import defaultdict
from typing import Dict

def frequency(s: str) -> Dict[str, int]:
  freqDict = defaultdict(int)
  for c in s:
    freqDict[c] += 1
  return dict(freqDict)

def reverse(freqDict: Dict[str, int]) -> Dict[int, str]:
  """key: number of appearance, value: string"""
  revDict = defaultdict(list)
  for k, v in freqDict.items():
    revDict[v].append(k)
  return dict(revDict)

def isValid(s: str):
  freqDict = frequency(s)
  revDict = reverse(freqDict)

  keys = list (revDict.keys())
  l = len(keys)
  if l == 1:
    return 'YES'
  if l > 2:
    return 'NO'
  if keys[0] < keys[1]:
    shortKey = keys[0]
    longKey = keys[1]
  else:
    shortKey = keys[1]
    longKey = keys[0]
  if shortKey == longKey - 1 and len(revDict[longKey]) == 1:
    return "YES"
  else:
    return "NO"