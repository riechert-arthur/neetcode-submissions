class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set() 
        for row in board:
            for cell in row:
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
            seen.clear()
        seen.clear()
        
        for i in range(len(board[0])):
            for j in range(len(board)):
                cell = board[j][i]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
            seen.clear()

        seen.clear()
        for base_row in range(3):
            for base_col in range(3):
                for i in range(base_row * 3, base_row * 3 + 3):
                    for j in range(base_col * 3, base_col * 3 + 3):
                        cell = board[i][j]
                        if cell != '.' and cell in seen:
                            return False
                        seen.add(cell)
                seen.clear()

        return True