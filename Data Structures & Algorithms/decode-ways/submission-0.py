class Solution:
    def numDecodings(self, s: str) -> int:
        alphabet = {
            '1': 'A',
            '2': 'B',
            '3': 'C',
            '4': 'D',
            '5': 'E',
            '6': 'F',
            '7': 'G',
            '8': 'H',
            '9': 'I',
            '10': 'J',
            '11': 'K',
            '12': 'L',
            '13': 'M',
            '14': 'N',
            '15': 'O',
            '16': 'P',
            '17': 'Q',
            '18': 'R',
            '19': 'S',
            '20': 'T',
            '21': 'U',
            '22': 'V',
            '23': 'W',
            '24': 'X',
            '25': 'Y',
            '26': 'Z',
        }

        n = len(s)
        counter = 0

        def dfs(i):

            nonlocal counter

            if not i < n:
                counter += 1
                return

            if i < n - 1 and s[i:i+2] in alphabet:
                dfs(i + 2)
            
            if i < n and s[i] in alphabet:
                dfs(i + 1)

        dfs(0)
        return counter

            