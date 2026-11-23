from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = defaultdict(list)

        for num in freq.keys():
            buckets[freq[num]].append(num)

        res = []

        for i in range(max(freq.values()), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res
        
        return res

        