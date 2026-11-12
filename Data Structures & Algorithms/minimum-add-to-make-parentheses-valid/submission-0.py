class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # every openning needs a closing:
        openings = 0
        res = 0
        for c in s:
            if c == "(":
                openings += 1
            else:
                if openings > 0:
                    openings -= 1
                else:
                    res += 1
        return res + openings
