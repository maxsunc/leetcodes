class Solution:
    def isPalindrome(self, s: str) -> bool:
        # determine if its a valid palindrom

        # case insensative
        l,r = 0, len(s) - 1

        while r > l:
            # skip stuff that isnt alnum
            while len(s) > l and (not s[l].isalnum()):
                l += 1
            while 0 <= r and not s[r].isalnum():
                r -= 1
            if l >= r:
                break
            if s[l].lower() != s[r].lower():
                return False

            r -= 1
            l += 1
        return True