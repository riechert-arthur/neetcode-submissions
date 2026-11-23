# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sort_snapshots = []

        for pair_idx in range(len(pairs)):
            left = pair_idx - 1
            right = pair_idx
            while left >= 0 and pairs[left].key > pairs[right].key:
                tmp = pairs[left]
                pairs[left] = pairs[right]
                pairs[right] = tmp
                left -= 1
                right -= 1

            sort_snapshots.append(pairs[:])

        return sort_snapshots