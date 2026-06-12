class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        max_profit = 0
        cheapest = prices[0]
        left = 0
        for right in range(1, len(prices)):
            max_profit = max(max_profit, prices[right]-cheapest)
            if prices[right] < cheapest:
                left = right
                cheapest = prices[right]

        return max_profit
                