"""
Function substring(str1: string, str2: string) -> Bool
Returns
  True -> str2 is a substring of str1
  False -> otherwise

Analysis
Sample Input

str1 = "abcdabcfg"
str2 = "cda"

for char in str1:
  if char == c:
    if str2[1:] == str1[place from c:]


Function distance()
Function substring(str1: string, str2: string) -> (int, int)
str1 = "abcdefg"
str2 = "bc"
str3 = "f"

substring("abcdefg", "bc") -> (1, 2)
substring("abcdefg", "f") -> (5, 5)
str1[2+1:5]

Write queue
with specific length

class queue:
  frist: Node(1)
  capacity: 5
  length: 5
  data: Node(1) <-> Node(2) <-> Node(3) <-> Node(4) <-> Node(5) <- Node(6)
  
  Function enqueue(elem: Node(int)):
    elem.next = this.data # Node(5) <- Node(6)
    this.data = elem.next # reassigning data to Node(6)
    if len(this.data) > this.capacity:
      dropFirst()
  
  Function dropFirst():
    first

"""


