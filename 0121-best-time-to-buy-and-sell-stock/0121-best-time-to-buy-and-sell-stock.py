class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p, profit = prices[0], 0
        for i in prices[1:]:
            if(i < p): p = i
            else: profit = max(profit, i-p)
        return profit