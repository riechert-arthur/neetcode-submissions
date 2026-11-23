class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        # The cost to get just past floor i
        T = [0] * n
        T[0] = cost[0]
        T[1] = cost[1]

        for i in range(2, n):
            T[i] = min(T[i - 1], T[i - 2]) + cost[i]

        return min(T[n - 1], T[n - 2])