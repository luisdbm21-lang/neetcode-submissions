class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Whatever smaller element we get next will logically lead to a bigger profit margin
            # than the last calculated min_value, if there is one to be found
        min_value = prices[0]

        for i in range(1, len(prices)):
            min_value = min(prices[i], min_value)
            max_profit = max(prices[i] - min_value, max_profit)

        return max_profit