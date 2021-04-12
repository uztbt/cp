import WriteAFunction2
import pytest

@pytest.mark.parametrize("input,want", [
  (1990, False),
  (2020, True),
])

def testIsLeap(input, want):
  assert WriteAFunction2.is_leap(input) == want