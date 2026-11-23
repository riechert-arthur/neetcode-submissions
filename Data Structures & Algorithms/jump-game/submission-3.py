class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = len(nums) - 2
        g = len(nums) - 1

        while i >= 0:
            if i + nums[i] >= g:
                g = i
            i -= 1
            print(g)

        return g == 0