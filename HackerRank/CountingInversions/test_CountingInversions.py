from CountingInversions2 import countInversions
import pytest

@pytest.mark.parametrize("input,want", [
  ([1, 1, 1, 2, 2], 0),
  ([2, 1, 3, 1, 2], 4),
  ([1, 5, 3, 7], 1)
])

def test(input, want):
  assert countInversions(input) == want