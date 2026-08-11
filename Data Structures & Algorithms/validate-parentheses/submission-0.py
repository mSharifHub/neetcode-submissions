class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { 
            ")":"(",
             "}":"{",
             "]":"["
          }   

        for close in s:
            if close in closeToOpen:
                if stack and stack[-1] == closeToOpen[close]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(close)

        return True if not stack else False
