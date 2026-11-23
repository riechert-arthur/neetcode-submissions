class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, working):
            
            # 3 Cases
            # Add the number with itself
            # Add the number with the new index
            # Skip this number

            # Working set if we chose to use the current number
            print(working)

            if curr == target:
                res.append(working[:])
                return
            
            if i >= len(nums) or curr > target:
                return

            # Skip
            dfs(i, curr + nums[i], working + [nums[i]])

            dfs(i + 1, curr, working[:])


        dfs(0, 0, [])

        return res