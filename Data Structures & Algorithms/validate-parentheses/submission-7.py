class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
        hashmap = {}
        hashmap[')'] = '('
        hashmap['}'] = '{'
        hashmap[']'] = '['

        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap.keys():
                print(stack)
                if not stack or stack.pop() != hashmap[char]:
                    return False
            else:
                return False
        
        return stack == []