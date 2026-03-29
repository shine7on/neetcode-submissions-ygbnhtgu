class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += s
            res += '-'

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        temp = ''

        for char in s:
            if char != '-':
                temp += char
            else:
                res.append(temp)
                temp = ''
        
        return res

