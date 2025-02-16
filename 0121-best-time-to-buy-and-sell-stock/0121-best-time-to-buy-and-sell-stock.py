class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]
        for price in prices[1:]:
            if price < low:
                low = price
            else:
                if price - low > max_profit:
                    max_profit = price - low
        return max_profit