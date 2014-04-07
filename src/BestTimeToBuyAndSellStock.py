class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        buy = 0x7FFFFFFF
        for price in prices:
            profit = max(profit, price-buy)
            buy = min(buy, price)
        return profit