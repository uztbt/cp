from ArrayManipulation2 import arrayManipulation
import pytest

@pytest.mark.parametrize("n,queries,want", [
  (5, [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
  ],
  200)
])

def test(n, queries, want):
  assert arrayManipulation(n, queries) == want