# A common problem for compilers and text editors is determining whether the parentheses
# in a string are balanced and properly nested. For example, the string ((())())() contains 
# properly nested pairs of parentheses, which the strings )()( and ()) do not. 
# Give an algorithm that returns true if a string contains properly nested and balanced parentheses

def isValidParentheses(call_stack):
  OPEN = '('
  stack = []
  for char in call_stack:
    if char is OPEN:
      stack.append(char)
    else:
      if len(stack) > 0:
        stack.pop()
      else:
        return False
  return len(stack) is 0

if __name__ == "__main__":
  assert isValidParentheses('((())())()') == True
  assert isValidParentheses(')()(') == False
  assert isValidParentheses('())') == False
