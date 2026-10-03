class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(cur):
            if cur == 0:
                return 1
            elif cur < 0:
                return 0
            if cur in memo:
                return memo[cur]
            val = dp(cur -1) + dp(cur - 2)
            memo[cur] = val
            return val
        
        return dp(n)
