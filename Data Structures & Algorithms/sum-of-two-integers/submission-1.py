class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        UNSIGNED = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        carry = 0
        c = 0
        for i in range(0, 32):
            a_i = a & 1
            b_i = b & 1
            c |= ((a_i ^ b_i ^ (carry & (c >= 0))) << i)
            carry = (a_i & b_i) | (a_i & carry) | (b_i & carry)

            a >>= 1
            b >>= 1

        c &= MASK

        return c if c <= UNSIGNED else ~(c ^ MASK)