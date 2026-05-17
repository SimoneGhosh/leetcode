class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        if (len(prices)) <= 1:
            return 0

        for r in range (1,len(prices)):
            if prices[r] < prices[l] and r<len(prices)-1:
                l = r 
                r = l+1
            
            profit = max (profit, prices[r]-prices[l])

        return profit