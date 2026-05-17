class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        if (len(prices)) <= 1:
            return 0

        for sell in prices:
            profit = max (profit, sell-minBuy)
            if minBuy > sell:
                minBuy = sell
        return profit