import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Assuming h >= len(piles)
        # Upper bound
        upper = max(piles)
        lower = 1

        k = upper

        # Strategy:
        # Check midpoint between 0 and r
        def recurse(l, r):

            nonlocal k

            print(f"({l},{r})")

            if l > r:
                return

            m = (l + r) // 2

            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / m)


            if hrs > h:
                recurse(m + 1, r)
            else:
                k = min(m, k)
                recurse(l, m - 1)

        recurse(lower, upper)

        return k