import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_x = -heapq.heappop(stones)
            stone_y = -heapq.heappop(stones)

            print(stone_x, stone_y)

            if stone_x != stone_y:
                heapq.heappush(stones, -abs(stone_x - stone_y))

        return -stones[0] if len(stones) == 1 else 0