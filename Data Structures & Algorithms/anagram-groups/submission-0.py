class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = {}
        
        for a_str in strs:
            a_hash = 1
            for char in a_str:
                a_hash *= ord(char) * ord(char)

            if a_hash not in hashes:
                hashes[a_hash] = []

            hashes[a_hash].append(a_str)

        print(hashes)

        res = []
        for key in hashes.keys():
            res.append(hashes[key])

        return res

