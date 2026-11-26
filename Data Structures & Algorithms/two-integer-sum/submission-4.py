from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(list) 

        for i, num in enumerate(nums):
            indices[num].append(i)

        for i, num in enumerate(nums):
            diff = target - num
            curr = indices[diff]
            for j in curr:
                if i != j:
                    return [i, j]