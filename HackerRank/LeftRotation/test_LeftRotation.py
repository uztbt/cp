import LeftRotation2
import pytest

@pytest.mark.parametrize("a,d,want", [
  ([1,2,3,4,5], 4, [5, 1, 2, 3, 4]),
  ([1,2], 2, [1,2]),
])

def testRotLeft(a, d, want):
  assert LeftRotation2.rotLeft(a, d) == want