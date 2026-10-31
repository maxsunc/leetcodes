class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return false if you can construct the ransom note from magazine

        occ = {}

        for c in magazine:
            occ[c] = occ.get(c,0) + 1
        
        for c in ransomNote:
            if occ.get(c,0) == 0:
                return False
            occ[c] -= 1
        return True