from TwoStrings2 import twoStrings
import pytest

@pytest.mark.parametrize("s1,s2,want", [
  ("hello", "world", "YES"),
  ("abc", "def", "NO")
])

def testAbbreviation(s1, s2, want):
  assert twoStrings(s1, s2) == want