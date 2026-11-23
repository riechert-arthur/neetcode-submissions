from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_map = defaultdict(lambda: defaultdict(int))

        for string in strs:
            if string in word_map:
                continue
            for char in string:
                word_map[string][char] += 1

        res = []

        for word in strs:
            added = False
            for li in res:
                if word_map[li[0]] == word_map[word]:
                    li.append(word)
                    added = True
                    break
            if not added:
                res.append([word])
        return res