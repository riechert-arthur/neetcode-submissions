class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for _ in nums]
        post = [1 for _ in nums]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        output = [post[i] * pre[i] for i in range(len(nums))]

        return output