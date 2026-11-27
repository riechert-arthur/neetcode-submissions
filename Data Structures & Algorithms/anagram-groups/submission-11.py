from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = defaultdict(list) 
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            freq[tuple(counts)].append(word) 

        return [freq[group] for group in freq.keys()]