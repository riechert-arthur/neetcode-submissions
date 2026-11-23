class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual = 0

        for num in nums:
            actual += num

        expected = 0

        for num in range(0, len(nums) + 1):
            expected += num

        return abs(expected - actual)