class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)     
        nums = sorted(nums)

        res = []

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            
            target = -nums[i]

            l, r = i + 1, n - 1

            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1

        return res