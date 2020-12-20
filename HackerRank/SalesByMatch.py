#!/bin/python3

import os
from typing import List

def sock_merchant(n: int, ar: List[int]) -> int:
  acc = 0
  table = [False] * 100
  
  for item in ar:
    index = item - 1
    v = table[index]
    table[index] = not v
    if v:
      acc += 1

  return acc

if __name__ == "__main__":
  n = int(input())

  ar = list(map(int, input().rstrip().split()))

  result = sock_merchant(n, ar)

  print(result)