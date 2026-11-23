class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # everycahracter of t needs to be in a windo of s
        # find the min length substring

        # ADOBECODEBANC
        # ABC
        # 

        # comparing the occurances is constant time operation O(26)
        # maintain a sliding window, if we're at the occurance then reducde the windwo size until we arent.
        # does this check all the substrings where it contains all occurance of t?

        # 

        l = 0
        tOcc = {}
        for c in t:
            tOcc[c] = tOcc.get(c,0) + 1

        sOcc = {}


        have,need = 0, len(tOcc) # have and need system by the unique occurances of characters

        def inSubstring():
            for key in tOcc:
                if sOcc.get(key,0) < tOcc[key]:
                    return False
            return True
                
        res = (-1,-1)
        for r in range(0, len(s)):
            c = s[r]
            sOcc[c] = sOcc.get(c,0) + 1
            # did we meet the requirement
            if sOcc[c] == tOcc.get(c,0):
                have += 1
            # does our substring contain all of t?
            while have == need:
                
                if res == (-1,-1):
                    res = (l, r)
                else:
                    if res[1] - res[0] > r - l:
                        res = (l,r)
                # reduce and see if its still valid
                sOcc[s[l]] -= 1
                if sOcc[s[l]] < tOcc.get(s[l], 0):
                    have -= 1
                l += 1
                

        
        return s[res[0] : res[1] + 1]