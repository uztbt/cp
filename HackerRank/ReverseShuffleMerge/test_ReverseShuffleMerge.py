from ReverseShuffleMerge import reverseShuffleMerge
import pytest

@pytest.mark.parametrize("input,want", [
  ("eggegg", "egg"),
  ("abcdefgabcdefg", "agfedcb"),
  ("aeiouuoiea", "aeiou")
])

def testReverseShuffleMerge(input, want):
  assert reverseShuffleMerge(input) == want