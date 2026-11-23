class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l, r = 0, 0
        curr_max = 0
        max_sum = 0

        while r < len(s):
            c = s[r]
            counts[c] = counts.get(c, 0) + 1
            curr_max = max(counts[c], curr_max)

            while (r - l + 1) - curr_max > k:
                counts[s[l]] -= 1
                l += 1
            
            max_sum = max(max_sum, r - l + 1)
            r += 1
            
        return max_sum