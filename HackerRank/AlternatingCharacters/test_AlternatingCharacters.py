from AlternatingCharacters2 import alternatingCharacters
import pytest

@pytest.mark.parametrize("input,want", [
  ("AAAA", 3),
  ("BBBBB", 4),
  ("ABABABA", 0),
  ("AAABBB", 4)
])

def test(input, want):
  assert alternatingCharacters(input) == want