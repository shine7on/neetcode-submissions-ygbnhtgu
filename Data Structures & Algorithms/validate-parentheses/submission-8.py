class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            elif stack and closeToOpen[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if not stack:
             return True

        return False
    