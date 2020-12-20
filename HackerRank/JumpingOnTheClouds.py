#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    def jump(i):
      """Retuns the next position"""
      if i >= n-3:
        return n-1
      elif c[i+2] == 0:
        return i + 2
      else:
        return i + 1
    jumps = 0
    position = 0
    while True:
      position = jump(position)
      jumps += 1
      if position >= n - 1:
        return jumps

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
