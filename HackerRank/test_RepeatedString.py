import RepeatedString

testCases = [
  {
    'input': ('aba', 10),
    'want': 7
  },
  {
    'input': ('a', 1000000000000),
    'want': 1000000000000
  }
]
def testAnswer():
  for case in testCases:
    ord
    assert RepeatedString.repeatedString(*case['input']) == case['want']
  