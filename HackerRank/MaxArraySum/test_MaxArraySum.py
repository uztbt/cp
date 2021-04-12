from MaxArraySum import maxSubsetSum
import pytest

@pytest.mark.parametrize("input,want", [
  ([-2, 1, 3, -4, 5], 8),
  ([3, 7, 4, 6, 5], 13)
])

def testMaxSubsetSum(input, want):
  assert maxSubsetSum(input) == want