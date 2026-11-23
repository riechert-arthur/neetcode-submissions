class Solution:
    delim = "\n"

    def encode(self, strs: List[str]) -> str:
        # space delimited

        res = ""

        for s in strs:
            res += s + self.delim

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""
        for c in s:
            if c == self.delim:
                res.append(curr)
                curr = ""
            else:
                curr += c

        return res
