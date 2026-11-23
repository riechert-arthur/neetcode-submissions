class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1 for _ in range(n)] for _ in range(m)]

        def dfs(_m, _n):

            if _m == m or _n == n:
                return

            paths[_m][_n] = \
                paths[_m - 1][_n] + \
                paths[_m][_n - 1]

            dfs(_m + 1, _n)
            dfs(_m, _n + 1)
        
        dfs(1, 1)

        return paths[m - 1][n - 1]