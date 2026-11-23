import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Decision Problem
        # - Does it meet the definition of a palindrome?
        # Palindrome:
        # - 
        # toLowercase
        # trim
        #
        # Reversing the string
        # Two pointers


        # [tat]
        # [taat]
        #   ^^
        #   ij
        
        temp = re.split(r"[^A-Za-z0-9]+", s)
        s = "".join(temp)
        s = s.lower()

        print(s)

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True