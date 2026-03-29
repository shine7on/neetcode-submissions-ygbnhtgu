class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.lower()
        resReverse = ''
        for char in res:
            if not char.isalnum():
                res = res.replace(char,'')
            else:
                resReverse = char + resReverse
        return res == resReverse