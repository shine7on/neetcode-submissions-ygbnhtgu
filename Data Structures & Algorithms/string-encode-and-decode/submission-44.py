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
        # unshift back to original payload
        original = "".join(chr(ord(c) - ord("a")) for c in s)

        res = []
        i = 0
        while i < len(original):
            # read length
            j = i
            while original[j] != "#":
                j += 1
            length = int(original[i:j])

            # read word of that length
            j += 1  # move past '#'
            word = original[j:j + length]
            res.append(word)

            # move i to next chunk
            i = j + length

        return res