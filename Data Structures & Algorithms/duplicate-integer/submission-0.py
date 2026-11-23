class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Binary
        # nums is not necessarily order

        # If an element is in the found set return...
        found = set()
        
        for num in nums:
            if num in found:
                return True
            found.add(num)

        return False