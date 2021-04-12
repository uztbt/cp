from Abbreviation import abbreviation
import pytest

@pytest.mark.parametrize("a,b,want", [
  ("daBcd", "ABC", "YES"),
])

def testAbbreviation(a, b, want):
  assert abbreviation(a, b) == want