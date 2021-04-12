from LargestRectangle import largestRectangle
import pytest

@pytest.mark.parametrize("h,want", [
  ([1,2,4,3,2,5,2,1], 12),
  ([11, 11, 10, 10, 10], 50)
])

def test(h, want):
  assert largestRectangle(h) == want