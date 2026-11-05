class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # for 1d DP: Try all possible coins at each total state
        # This is same speed as 2d dp: It may have less states but the work for each state is now n instead of constant
        res = math.inf
        memo = {}

        def dp(total):
            nonlocal res
            if total == amount:
                return 0
            if total > amount:
                return math.inf
            if total in memo:
                return memo[total]
            val = math.inf
            for i in range(0, len(coins)):
                val = min(val, dp(total + coins[i]) + 1)
            memo[total] = val
            return val
        res = dp(0)
        return res if res != math.inf else -1