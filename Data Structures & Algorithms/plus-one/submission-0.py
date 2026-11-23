class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        if digits[-1] + 1 == 10:
            carry = 1
            digits[-1] = 0
        else:
            digits[-1] += 1
            return digits

        print([i for i in range(len(digits) - 1, 0, -1)])

        for i in range(len(digits) - 2 , -1, -1):
            
            if carry != 1:
                break

            if digits[i] + 1 == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0

        if carry == 1:
            digits.insert(0, 1)

        return digits