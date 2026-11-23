class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for num in nums:
            if not num - 1 in nums:
                x = num
                curr_count = 1
                while x + 1 in nums:
                    curr_count += 1
                    x += 1
                max_count = max(curr_count, max_count)
        
        return max_count