class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyIndex = 0
        res = 0

        for i, price in enumerate(prices):
            if prices[i] < prices[buyIndex]:
                buyIndex = i
            res = max(res, price - prices[buyIndex])
        return res