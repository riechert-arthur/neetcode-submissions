class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        curr = ""
        ref = sorted(word)
        found = False
        visited = [[False for _ in board[0]] for _ in board]

        def dfs(i, j):

            nonlocal curr
            nonlocal found

            if curr == word:
                found = True

            if found:
                return found

            if i < 0 or i >= len(board):
                return False

            if j < 0 or j >= len(board[i]) or visited[i][j]:
                return False

            curr += board[i][j]

            if not word.startswith(curr):
                curr = curr[:-1]
                return False

            visited[i][j] = True

            r1 = dfs(i + 1, j)
            r2 = dfs(i, j + 1)
            r3 = dfs(i - 1, j)
            r4 = dfs(i, j - 1)

            visited[i][j] = False
            curr = curr[:-1]
            return r1 or r2 or r3 or r4

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j):
                    return True

        return False