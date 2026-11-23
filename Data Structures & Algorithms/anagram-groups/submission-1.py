class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = {}
        
        for a_str in strs:
            a_hash = [0] * 26
            for char in a_str:
                a_hash[ord(char) % 26] += 1

            if tuple(a_hash) not in hashes:
                hashes[tuple(a_hash)] = []

            hashes[tuple(a_hash)].append(a_str)

        print(hashes)

        res = []
        for key in hashes.keys():
            res.append(hashes[key])

        return res

