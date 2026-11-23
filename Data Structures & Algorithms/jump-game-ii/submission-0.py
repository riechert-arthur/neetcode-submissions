class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0

        # [2,4,1,1,1,1]
        for i in range(n - 2, -1, -1):
            dp[i] = min(dp[i:min(i + nums[i], n - 1)+1]) + 1
        
        print(dp)
        return dp[0]