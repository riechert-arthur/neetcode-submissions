class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def re(l, r):
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if l == r:
                return -1

            # Pivot on right
            if nums[m] > nums[r]:
                if target < nums[m] and target >= nums[l]:
                    return re(l, m)
                return re(m + 1, r)
            # Pivot on left
            else:
                if target > nums[m] and target <= nums[r]:
                    return re(m + 1, r)
                return re(l, m)

        return re(0, len(nums) - 1)