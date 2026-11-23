from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        tuples = []
        for num in freq.keys():
            tuples.append((num, freq[num]))
        
        n = len(tuples)
        tuples.sort(key=lambda x: x[1])
        return [x[0] for x in tuples[n - k:n]]