class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()

        for char in s:
            if char.isalpha() == False and char.isdigit() == False:
                s = s.replace(char, "")

        rev = ""

        for i in range(len(s)-1, -1, -1):
            rev += s[i]

        return s == rev