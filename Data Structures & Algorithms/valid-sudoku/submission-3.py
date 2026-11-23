class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n, m = len(board), len(board[0])

        def validate_rows() -> bool:
            seen = set() 
            for i in range(n):
                for j in range(m):
                    cell = board[i][j] 
                    if cell != "." and board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
                seen.clear()
            return True

        def validate_cols() -> bool:
            seen = set()
            for j in range(m):
                for i in range(n):
                    cell = board[i][j]
                    if cell != "." and cell in seen:
                        return False
                    seen.add(board[i][j])
                seen.clear()
            return True 

        def validate_boxes() -> bool:
            seen = set()
            for k in range(9):
                for i in range(3):
                    for j in range(3):
                        row = ((k // 3) * 3) + i
                        col = ((k % 3) * 3) + j
                        print((row, col)) 
                        cell = board[row][col]
                        if cell != "." and cell in seen:
                            return False  
                        seen.add(cell)
                seen.clear()
            return True
        
        return validate_rows() \
            and validate_cols() \
            and validate_boxes()