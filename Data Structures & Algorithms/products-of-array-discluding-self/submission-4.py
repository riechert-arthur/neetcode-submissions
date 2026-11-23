class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        asc_multiples = [0 for _ in range(n)]
        desc_multiples = asc_multiples[:]

        for i in range(n):
            if i == 1 and nums[i - 1] != 0:
                asc_multiples[i] = nums[i - 1]
                continue
            asc_multiples[i] = nums[i - 1] * asc_multiples[i - 1]

        for i in range(n - 2, -1, -1):
            if i == n - 2 and nums[i + 1] != 0:
                desc_multiples[i] = nums[i + 1]
                continue
            desc_multiples[i] = nums[i + 1] * desc_multiples[i + 1]

        print(asc_multiples, desc_multiples)

        res = []
        for i in range(n): 
            if i == 0 or i == n - 1:
                res.append(max(asc_multiples[i], desc_multiples[i]) or min(asc_multiples[i], desc_multiples[i]))
                continue
            res.append(asc_multiples[i] * desc_multiples[i])

        return res