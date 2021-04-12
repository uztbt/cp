class MyQueue:
  def __init__(self):
    super().__init__()
    self.stack1: list = []
    self.stack2: list = []

  def put(self, value):
    self.stack1.append(value)

  def peek(self):
    if len(self.stack2) == 0:
      self.move()
    return self.stack2[-1]

  def pop(self):
    if len(self.stack2) == 0:
      self.move()
    self.stack2.pop()

  def move(self):
    while len(self.stack1) > 0:
      item = self.stack1.pop()
      self.stack2.append(item)