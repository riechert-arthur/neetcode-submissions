class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Store the last index we saw it t
        chars = {}
        ref = {}
        nums_found = 0

        l, r = 0, 0

        for t_i in t:
            ref[t_i] = ref.get(t_i, 0) + 1

        while r < len(s) and nums_found < len(t):
            chars[s[r]] = chars.get(s[r], 0) + 1
            if s[r] in ref and chars[s[r]] <= ref[s[r]]:
                nums_found += 1
            r += 1

        if nums_found < len(t):
            return ""

        while l < r and (s[l] not in ref or chars[s[l]] > ref[s[l]]):
            chars[s[l]] -= 1
            l += 1

        l_min, r_min = l, r
        while r < len(s):
            chars[s[r]] = chars.get(s[r], 0) + 1
            while chars[s[l]] - 1 >= ref.get(s[l], 0):
                chars[s[l]] -= 1
                l += 1
            
            new_length = r - l + 1
            old_length = r_min - l_min

            if new_length < old_length:
                r_min = r + 1
                l_min = l

            r += 1

        print(l_min)
        return s[l_min : r_min]