class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        def _binary_search(left: int, right: int):

            nonlocal matrix
            nonlocal target
            nonlocal m
            nonlocal n

            mid = (left + right) // 2
            row = mid // n
            col = mid % n

            print(f"mid: {(left + right) / 2}")
            print(f"left: {left} | right: {right}")
            print(f"row: {row} | col: {col}")

            if right <= left:
                return matrix[row][col] == target

            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                return _binary_search(left, mid)
            else:
                return _binary_search(mid + 1, right)

        return _binary_search(0, n * m - 1)