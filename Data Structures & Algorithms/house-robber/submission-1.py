class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        m = [nums[0] for _ in nums]

        # 2 choices
        # -> Rob
        # -> Don't rob
        m[0] = nums[0]
        m[1] = max(m[0], nums[1])

        for i in range(2, len(nums)):
            m[i] = max(m[i - 1], nums[i] + m[i - 2])

        print(m)
        return m[-1]