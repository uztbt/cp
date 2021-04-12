from MyQueue2 import MyQueue
import pytest


@pytest.mark.parametrize("arr,want", [
  ([["1", "42"], ["2"], ["1", "14"], ["3"], ["1", "28"], ["2"], ["1", "60"], ["3"], ["2"], ["2"]], ["14", "28"])
])

def test(arr, want):
  q = MyQueue()
  res = []
  for item in arr:
    command = item[0]
    if command == "1":
      q.put(item[1])
    elif command == "2":
      q.pop()
    elif command == "3":
      res.append(q.peek())
  assert res == want