from UtopianTree import utopianTree
import pytest
@pytest.mark.parametrize("input,want", [
  (0, 1),
  (1, 2),
  (4,7)
  ]
)

def testUtopianTree(input, want):
  assert utopianTree(input) == want