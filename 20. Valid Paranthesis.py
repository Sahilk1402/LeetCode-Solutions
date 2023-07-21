class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
          ')': '(',
          '}': '{',
          ']': '['
        }
        for char in s:
          if char in d.values():
            stack.append(char)
          elif (not stack) or (stack.pop() != d[char]):
              return False
        return len(stack) == 0
