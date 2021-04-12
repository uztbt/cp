from MinMaxRiddle import riddle
import pytest

@pytest.mark.parametrize("arr,want", [
  ([6, 3, 5, 1, 12], [12, 3, 3, 1, 1]),
  ([2], [2])
])

def test(arr, want):
  assert riddle(arr) == want