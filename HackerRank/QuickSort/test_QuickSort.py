from QuickSort import quicksort, quicksortMutating
import pytest


@pytest.mark.parametrize("arr,want", [
  ([3, 1, 8, 6, 9, 3, 5, 2], [1, 2, 3, 3, 5, 6, 8, 9])
])

def test(arr, want):
  quicksortMutating(arr, 0, len(arr)-1)
  assert arr == want