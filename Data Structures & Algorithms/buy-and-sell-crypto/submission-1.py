class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        index = 0
        
        for i in prices:
            for j in prices[index:]:
                if j - i > max_profit:
                    max_profit = j - i
            index += 1

        return max_profit