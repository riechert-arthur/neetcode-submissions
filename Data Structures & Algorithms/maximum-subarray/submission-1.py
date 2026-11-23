class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0] for _ in nums]

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        print(dp)

        return max(dp)