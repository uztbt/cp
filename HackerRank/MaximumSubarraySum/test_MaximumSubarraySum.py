from MaximumSubarraySum import maximumSum
import pytest

@pytest.mark.parametrize("arr,m,want", [
  ([3, 3, 9, 9, 5], 7, 6),
  ([1, 5, 9], 5, 4)
])

def test(arr, m, want):
  assert maximumSum(arr, m) == want