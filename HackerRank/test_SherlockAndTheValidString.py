import SherlockAndTheValidString2

def testFreq():
  testCases = [
    {
      'input': "abbaab",
      'want': {'a': 3, 'b': 3}
    }
  ]

  for case in testCases:
    assert dict(SherlockAndTheValidString2.frequency(case['input'])) == case['want']

def testReverse():
  testCases = [
    {
      'input': {'a': 3, 'b': 3},
      'want': {3: ['a', 'b']}
    }
  ]
  for case in testCases:
    assert SherlockAndTheValidString2.reverse(case['input']) == case['want']

def testIsValid():
  testCases = [
    {
      'input': "aa",
      'want': "YES"
    },
    {
      'input': "abaa",
      "want": "NO"
    },
    {
      'input': "aabbccddeefghi",
      'want': 'NO'
    },
    {
      'input': "abcdefghhgfedecba",
      'want': 'YES'
    }
  ]
  for case in testCases:
    assert SherlockAndTheValidString2.isValid(case['input']) == case['want']