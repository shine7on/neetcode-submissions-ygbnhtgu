class Solution:

    def encode(self, strs: List[str]) -> str:
        original = ""

        for x in strs:
            original = original + x + "-"
        
        new = ""

        for char in original:
            new += chr(ord(char)+ord('a'))
        
        return new


    def decode(self, s: str) -> List[str]:
        result = []
        word = ""

        for x in range(len(s)):
            char = chr(ord(s[x])-ord("a"))
            if char == "-":
                result.append(word)
                word = ""
            else:
                word += char

        return result
    

