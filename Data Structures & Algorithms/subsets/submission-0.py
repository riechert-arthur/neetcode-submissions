from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # 2 cases
        # Include the num
        # Don't include the num

        res, path = [], []

        def dfs(i: int):
            
            if i == len(nums):
                res.append(path[:])
                return

            # Don't include
            dfs(i + 1)

            path.append(nums[i])

            dfs(i + 1)

            # Remove the used numbers to avoid duplication
            path.pop()

        dfs(0)

        return res