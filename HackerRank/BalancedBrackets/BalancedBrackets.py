def isBalanced(s: str):
  stack = list()
  for bracket in s:
    if bracket == '(' or bracket == '{' or bracket == '[':
      stack.append(bracket)
      continue
    if len(stack) == 0:
      # No reserve
      return "NO"
    openingBracket = stack.pop()
    if bracket == ')' and openingBracket != '(':
      return "NO"
    if bracket == '}' and openingBracket != '{':
      return "NO"
    if bracket == ']' and openingBracket != '[':
      return "NO"
  if len(stack) > 0:
    return "NO"
  else:
    return "YES"
        
    