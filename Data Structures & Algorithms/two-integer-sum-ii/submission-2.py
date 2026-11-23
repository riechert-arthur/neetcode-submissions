class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        curr_sum = 0

        print(i, j)
        while i < j:
            curr_sum = numbers[i] + numbers[j]
            diff = curr_sum - target

            if diff > 0:
                j -= 1
            elif diff < 0:
                i += 1
            else:
                break

        return [i + 1, j + 1]
