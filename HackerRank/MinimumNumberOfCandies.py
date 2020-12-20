""" 
Write a function which takes rating array as parameter and returns number of candies for the following problem.

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?
"""
from typing import List, Mapping

def distribution_order(r: List[int]) -> Mapping[int, int]:
  # Returns the order in which we give candies to the children
  return map(
    lambda item: item[0],
    sorted(enumerate(r), key=lambda item: item[1])
    )

def distribute_candies(r: List[int]) -> List[int]:
  # Returns the list of the numbers of candies each child gets from us
  n = len(r)
  if n == 1:
    return [1]

  c = [0] * n

  def candies_for(i):
    # Returns the number of candies i-th child gets from us
    if i == 0 and r[i] > r[i+1]:
      return c[i+1] + 1
    if i == n-1 and r[i] > r[i-1]:
      return c[i-1] + 1
    if (0 < i and i < n-1) and (r[i-1] < r[i] or r[i+1] < r[i]):
      return max(c[i-1], c[i+1]) + 1
    return 1
      
  for i in distribution_order(r):
    c[i] = candies_for(i)

  return c

def minumum_number_of_candies(r: List[int]) -> int:
  # Returns the total number of candies we have to give
  return sum(distribute_candies(r))

if __name__ == "__main__":
  candies = [int(item) for item in input("Enter ratings: ").split()]
  print(minumum_number_of_candies(candies))