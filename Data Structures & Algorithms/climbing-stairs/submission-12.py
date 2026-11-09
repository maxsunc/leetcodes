class Solution:
    def climbStairs(self, n: int) -> int:
        # n steps

        # bottom up:
        # create an array of length n
        if n <= 2:
            return n
        
        first,prev = 2,1
        for i in range(2, n):
            tmp = first
            first = first + prev
            prev = tmp
        return first