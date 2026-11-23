class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_str = "" 
        
        for chunk in strs:
            char_count = len(chunk)

            encoded_str += f'{char_count},{chunk}' 

        return encoded_str

    def decode(self, s: str) -> List[str]:

        start_idx = 0
        idx = 0
        char_count = 0
        res = []

        while idx < len(s):
            while s[idx] != ',':
                idx += 1
            char_count = int(s[start_idx : idx])
            last_idx = idx + 1 + char_count
            res.append(s[idx + 1: last_idx])
            start_idx = last_idx
            idx = last_idx
            
        return res
            