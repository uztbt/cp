from collections import defaultdict
import itertools
from typing import Iterator

def signature(s: str) -> dict[str, int]:
  d = defaultdict(int)
  for c in s:
    d[c] += 1
  return d

def inside(str1: Iterator, str2: str) -> bool:
  index = -1
  for c in str1:
    index = str2.find(c, index+1)
    if index == -1:
      return False
  return True

def reverseShuffleMerge(s: str) -> str:
  sSignature = signature(s)
  aSample = ""
  for k, v in sSignature.items():
    aSample += k * (v // 2)
  asOrdered = itertools.permutations(sorted(aSample))
  lastOne = ""
  
  for a in asOrdered:
    if a == lastOne:
      continue
    revA = reversed(a)
    if inside(revA, s):
      return ''.join(a)
    lastOne = a
  return ""
  
