from types import FrameType
from MatchedItems import findMatchedItems
import pytest

@pytest.mark.parametrize("strings,target, want", [
  ([['A','B'],['A','B','C'],['B','D'],['B','C','D']], ['B', 'C'], [1, 3])
])

def test(strings, target, want):
  assert findMatchedItems(strings, target) == want