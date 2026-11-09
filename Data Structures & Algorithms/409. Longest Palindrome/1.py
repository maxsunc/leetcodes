class Solution:
    def longestPalindrome(self, s: str) -> int:
        # even length are free, if we find an odd length incrment our result by 1
        occ = {}
        res = 0
        oddBonus = 0
        for c in s:
            occ[c] = occ.get(c,0) + 1
        
        for key in occ:
            res += (occ[key] // 2) * 2
            if occ[key] % 2 == 1:
                oddBonus = 1
        return res + oddBonus
