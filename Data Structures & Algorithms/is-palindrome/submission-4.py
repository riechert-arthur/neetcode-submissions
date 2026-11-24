class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuation = set([',', '\'', '"', "-", ".", "?", ":", "!"])

        s = s.replace(" ", "").lower()
        print(s)

        l, r = 0, len(s) - 1
        while l < len(s) and r >= 0:
            if s[l] in punctuation:
                l += 1
                continue
            elif s[r] in punctuation:
                r -= 1
                continue

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True