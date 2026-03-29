class Solution:

    def encode(self, strs: List[str]) -> str:
        original = ""

        for x in strs:
            original = original + str(len(x)) + "#" + x
        
        new = ""

        for char in original:
            new += chr(ord(char)+ord("a"))
        
        return new


    def decode(self, s: str) -> List[str]:

        original = ""

        for char in s:
            original += chr(ord(char)-ord("a"))

        result = []
        word = ""
        length = 0
        start = 0
        end = 0

        while end < len(s):
            if original[end] != "#":
                end += 1
            else:
                length = int(original[start:end])
                word = original[end+1:end+1+length]
                result.append(word)
                word = ""
                start = end + 1 + length
                end = start

        return result
    

