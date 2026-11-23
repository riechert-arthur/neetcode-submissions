class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not board:
            return False
        
        # Scan rows
        for row in board:
            seen = set()
            for num in row:
                if num in seen:
                    print("false while scan rows")
                    return False
                
                if num != ".":
                    seen.add(num)

        # Scan columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    print("false while scan cols", i, j, seen)
                    return False
                
                if board[j][i] != ".":
                    seen.add(board[j][i])

        # Scan each box
        i_start, j_start = 0, 0
        while i_start < len(board) - 2 and j_start < len(board[0]) - 2:
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[i_start + i][j_start + j]
                    if num in seen:
                        print("false while scanning box")
                        return False
                    if num != ".":
                        seen.add(num)

            if not i_start + 3 >= len(board) - 2 and j_start + 3 >= len(board[0]) - 2:
                i_start += 3
                j_start = 0
            else:
                j_start += 3
                
        return True
