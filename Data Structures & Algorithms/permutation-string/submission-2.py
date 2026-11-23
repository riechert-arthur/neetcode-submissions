class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        # Sliding Window
        #
        # 1. Window size of 3

        ref = {chr(ord('a') + i): 0 for i in range(26)}
        
        for char in s1:
            ref[char] += 1

        ref2 = {chr(ord('a') + i): 0 for i in range(26)}
            
        for i in range(len(s1)):
            char = s2[i]
            ref2[char] += 1
            if ref2 == ref:
                return True

        for i in range(1, len(s2) - len(s1) + 1):
            j = i + len(s1) - 1
            ref2[s2[i - 1]] -= 1
            ref2[s2[j]] += 1

            print(ref2)

            if ref2 == ref:
                return True

        return False