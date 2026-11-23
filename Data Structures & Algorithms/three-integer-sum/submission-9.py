from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        # O nlogn
        nums = sorted(nums)

        if n == 0 \
            or nums[0] > 0:
            return []

        # Strategy:
        # Assume i_1 will be fixed
        # i_2 will always start 1 left from i_3
        # Break after i_2 crosses i_1

        # -4, -1, -1, 0, 1, 2
        
        i = 0
        prev = None
        for i, num in enumerate(nums):
            j, k = i + 1, n - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    tmp = [nums[i],nums[j],nums[k]]
                    if tmp != prev:
                        res.append(tmp)
                        prev = tmp
                    j += 1
                    k -= 1
                    

        return res