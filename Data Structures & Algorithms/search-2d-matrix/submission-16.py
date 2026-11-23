class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        def _binary_search(left: int, right: int):

            mid = (left + right) // 2
            row = mid // n
            col = mid % n

            if right <= left:
                return matrix[row][col] == target

            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                return _binary_search(left, mid)
            else:
                return _binary_search(mid + 1, right)

        return _binary_search(0, n * m - 1)