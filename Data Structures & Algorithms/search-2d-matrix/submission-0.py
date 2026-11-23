class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [v for row in matrix for v in row]
        
        def _binary_search(left: int, right: int):

            nonlocal flattened
            nonlocal target

            mid = (left + right) // 2

            if flattened[mid] == target:
                return True

            if left >= right:
                return False

            if flattened[mid] > target:
                return _binary_search(left, mid)
            else:
                return _binary_search(mid + 1, right)

        return _binary_search(0, len(flattened) - 1)