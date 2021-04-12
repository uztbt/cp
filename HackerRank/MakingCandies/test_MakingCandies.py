from MakingCandies import minimumPasses
import pytest

@pytest.mark.parametrize("m,w,p,n,want", [
  (3, 1, 2, 12, 3)
])

def test(m, w, p, n, want):
  assert minimumPasses(m, w, p, n) == want