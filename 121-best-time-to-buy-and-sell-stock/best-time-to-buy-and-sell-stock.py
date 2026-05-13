class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            curr = sell - minBuy

            if curr > maxProfit:
                maxProfit = curr
            
            if sell < minBuy:
                minBuy = sell
        return maxProfit