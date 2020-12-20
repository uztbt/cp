import RepeatedString
import unittest

class Test(unittest.TestCase):
  table = [
    {
      'input': ("abcac", 12),
      'want': 5
    }
  ]

  def test(self):
    for i, case in enumerate(self.table):
      with self.subTest(i=i):
        self.assertEqual(
          RepeatedString.repeatedString(*case['input']),
          case['want']
        )