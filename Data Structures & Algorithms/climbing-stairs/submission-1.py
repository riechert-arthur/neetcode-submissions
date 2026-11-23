class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        T = [0] * n
        T[0] = 1
        T[1] = 2
        
        for i in range(2, n):
            T[i] = T[i - 1] + T[i - 2]

        return T[n - 1]