class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        G = [[1 for _ in grid[0]] for _ in grid]
        n = 0

        def dfs(i, j):

            nonlocal G
            nonlocal grid

            if i < 0 \
                or i >= len(G) \
                or j < 0 \
                or j >= len(G[i]) \
                or G[i][j] == 0 \
                or grid[i][j] == '0':
                return

            G[i][j] = 0

            # 0, 1, 0, 0, 0
            # 0, 1, 0, 1, 0
            # 0, 0, 0, 1, 0

            # 1, 0, 1, 1, 1
            # 1, 0, 1, 0, 1
            # 1, 1, 1, 0, 1

            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i, g_i in enumerate(grid):
            for j, g_j in enumerate(g_i):
                if g_j == '1' and G[i][j] != 0:
                    n += 1
                    dfs(i, j)
                    print(G)

        return n