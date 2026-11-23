class Solution:
    def reverseBits(self, n: int) -> int:

        n_reversed = int(0)

        for _ in range(31):
            n_reversed |= (n & 1)
            n_reversed <<= 1
            n >>= 1

        n_reversed |= (n & 1)

        return n_reversed