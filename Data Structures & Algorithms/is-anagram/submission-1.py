class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # A decision
        # How to meet the definition of an anagram:
        # - the same set of characters
        # - each character would have the same quanity

        T_s = {}
        T_t = {}

        for s_i in s:
            if s_i not in T_s:
                T_s[s_i] = 1
            else:
                T_s[s_i] += 1

        for t_i in t:
            if t_i not in T_t:
                T_t[t_i] = 1
            else:
                T_t[t_i] += 1

        print(f"T_s: {T_s}")
        print(f"T_t: {T_t}")

        # Check results of s against t
        return T_s == T_t