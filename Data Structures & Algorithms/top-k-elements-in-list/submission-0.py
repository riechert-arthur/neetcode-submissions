class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums))]
        frequencies_temp = {}

        for num in nums:
            if not num in frequencies_temp:
                frequencies_temp[num] = 0
            frequencies_temp[num] += 1

        print(frequencies_temp)

        for num in frequencies_temp.keys():
            frequencies[frequencies_temp[num] - 1].append(num)

        print(frequencies)

        res = []

        for freq in frequencies[::-1]:
            for num in freq:
                res.append(num)
                if len(res) == k:
                    break
            
            if len(res) == k:
                break

        return res
