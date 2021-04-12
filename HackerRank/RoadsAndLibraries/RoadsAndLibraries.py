from collections import defaultdict
import functools

def roadmap(cities: list[list[int]]) -> dict[int, set[int]]:
  d = defaultdict(set)
  for item in cities:
    d[item[0]].add(item[1])
    d[item[1]].add(item[0])
  return d

def roadsAndLibraries(n: int, c_lib: int, c_road: int, cities: list[list[int]]) -> int:
  rmap = roadmap(cities)
  
  if c_lib <= c_road:
    # Construct a library in each city
    return n * c_lib
  
  visited = set()
  n_lib = 0
  n_road = 0
  
  def formTree(s: int) -> int:
    acc = 0
    for city in rmap[s]:
      if city in visited:
        continue
      visited.add(city)
      acc += 1
      acc += formTree(city)
    return acc
  
  for city in range(1, n+1):
    if city in visited:
      continue
    visited.add(city)
    n_lib += 1
    n_road += formTree(city)

  return n_lib * c_lib + n_road * c_road