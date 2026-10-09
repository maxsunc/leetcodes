class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap,tMap = {}, {}

        for c in s:
            sMap[c] = sMap.get(c,0) + 1
        
        for c in t:
            tMap[c] = tMap.get(c,0) + 1
        
        for key in sMap:
            if sMap[key] != tMap.get(key,0):
                return False
        for key in tMap:
            if tMap[key] != sMap.get(key,0):
                return False
        return True