class Solution:
    def countBits(self, n: int) -> List[int]:

        def _bit_count(n: int) -> int:
            count = 0

            for _ in range(n):
                count += n & 1
                n >>= 1
            
            return count

        output = [0] * (n + 1)

        for i in range(0, n + 1):
            output[i] = _bit_count(i)

        return output