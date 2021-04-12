from CommonChild2 import commonChild
import pytest

@pytest.mark.parametrize("s1,s2,want", [
  ("HARRY", "SALLY", 2),
])

def test(s1, s2, want):
  assert commonChild(s1, s2) == want