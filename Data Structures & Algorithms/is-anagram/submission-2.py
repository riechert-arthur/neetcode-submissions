class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        n = len(s)
        idx = 0
        while idx < n:
            if sorted_s[idx] != sorted_t[idx]:
                return False
            idx += 1

        return True