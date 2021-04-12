from CompanyLogo2 import companyLogo
import pytest

@pytest.mark.parametrize("input,want", [
  ("aabbbccde", [("b", 3), ("a", 2), ("c", 2)])
])

def test(input, want):
  assert companyLogo(input) == want