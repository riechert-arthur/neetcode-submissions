class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # seen = [z]
        #
        # "zxyzxyz"
        #   ^    ^
        #   l    r    

        L_max = 0
        seen = set()
        i_left = 0

        for i_right, s_i in enumerate(s):
            while s_i in seen:
                seen.remove(s[i_left])
                i_left += 1
            
            if i_right - i_left + 1 > L_max:
                L_max = i_right - i_left + 1
            seen.add(s_i)

        return L_max