class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        count = 0

        for char in s:
            # first in, last out
            match (char):
                case ('{'):
                    count += 1
                    stack.append(char)
                case ("["):
                    count += 1
                    stack.append(char)
                case("("):
                    count += 1
                    stack.append(char)
                case ("}"):
                    if count == 0 or stack.pop() != "{":
                        return False
                    count -= 1
                case (")"):
                    if count == 0 or stack.pop() != "(":
                        return False
                    count -= 1
                case ("]"):
                    if count == 0 or stack.pop() != "[":
                        return False
                    count -= 1
                case _: # i forgor this syntax
                    return False
            # if char == '{' or char == "(" or char == "[":
            #    stack.append(char)
            

            # elif char == "}" and stack.pop() != "{":
            #    return False
            # elif char == ")" and stack.pop() != "(":
            #    return False
            # elif char == "]" and stack.pop() != "[":
            #    return False
            
        
        if stack != []:
            return False

        return True





                

            
