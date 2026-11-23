class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_r(nums, target, 0, len(nums) - 1)
        
    def search_r(self, nums:List[int], target: int, left: int, right: int) -> int:
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if left >= right:
            return -1

        if target < nums[mid]:
            return self.search_r(nums, target, left, mid)
        else:
            return self.search_r(nums, target, mid + 1, right)
        