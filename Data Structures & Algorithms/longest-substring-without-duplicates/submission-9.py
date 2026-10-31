class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window algorithm
        # has this vlaue been seen before? if it has remove from the back ( theres no way to proceed otherwirse)

        l = 0
        seen = set()
        res = 0

        for r in range(0,len(s)):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1

            seen.add(c)
            res = max(res, r - l + 1)
        return res
