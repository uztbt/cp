from RoadsAndLibraries import roadsAndLibraries
import pytest

@pytest.mark.parametrize("n,c_lib,c_road,cities,want", [
  (3, 2, 1, [[1,2], [3,1], [2, 3]], 4),
  (6, 2, 5, [
    [1, 3],
    [3, 4],
    [2, 4],
    [1, 2],
    [2, 3],
    [5, 6]
  ],
  12),
  (5, 6, 1, [[1, 2], [1, 3], [1, 4]], 15)
])

def test(n, c_lib, c_road, cities, want):
  assert roadsAndLibraries(n, c_lib, c_road, cities) == want