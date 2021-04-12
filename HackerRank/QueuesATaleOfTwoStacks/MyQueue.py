class MyQueue:
  def __init__(self):
      super().__init__()
      self.oldestTopStack = []
      self.newestTopStack = []

  def peek(self):
    self.move()
    return self.oldestTopStack[-1]

  def pop(self):
    self.move()
    return self.oldestTopStack.pop()

  def put(self, value):
    self.newestTopStack.append(value)

  def move(self):
    if len(self.oldestTopStack) == 0:
      while len(self.newestTopStack) > 0:
        self.oldestTopStack.append(self.newestTopStack.pop())