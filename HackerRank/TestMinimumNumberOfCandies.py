from MinimumNumberOfCandies import distribute_candies
import unittest

class Test(unittest.TestCase):

  table = [
    {
      'input': [0, 0, 0],
      'want': [1, 1, 1]
    },
    {
      'input': [0, 1, 0],
      'want': [1, 2, 1]
    },
    {
      'input': [0, 1, 2],
      'want': [1, 2, 3]
    },
    {
      'input': [0, 2, 1],
      'want': [1, 2, 1]
    },
    {
      'input': [1, 10, 8, 7, 0, 4, 3, 2],
      'want': [1, 4, 3, 2, 1, 3, 2, 1]
    },
    {
      'input': [5, 3, 2, 1, 1, 5],
      'want': [4, 3, 2, 1, 1, 2]
    }
  ]

  def test(self):
    for i, case in enumerate(self.table):
      with self.subTest(i=i):
        self.assertEqual(
          distribute_candies(case['input']),
          case['want']
        )

if __name__ == "__main__":
  unittest.main()