class Solution:
    def isHappy(self, n: int) -> bool:

        def _next_i(n: int) -> int:
            v_sum = 0
            while n > 0:
                i = n % 10
                print(i)
                n //= 10
                v_sum += i * i

            return v_sum

        if n == 1:
            return True

        i_slow = n
        i_fast = _next_i(n)

        while i_slow != i_fast:
            i_slow = _next_i(i_slow)
            i_fast = _next_i(i_fast)
            i_fast = _next_i(i_fast)

            if i_fast == 1:
                return True

        return False
