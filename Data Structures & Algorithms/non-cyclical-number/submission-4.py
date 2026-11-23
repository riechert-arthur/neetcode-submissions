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

        seen = set([n])
        i = _next_i(n)

        while not i in seen:
            seen.add(i)
            i = _next_i(i)
            if i == 1:
                return True

        return False
