class Solution:
    def findMin(self, nums: List[int]) -> int:

        def re(l, r):
            if l == r:
                return nums[l]

            m = (r + l) // 2

            if nums[m] > nums[r]:
                return re(m + 1, r)
            else:
                return re(l, m)

        return re(0, len(nums) - 1)