class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None:
            return 0
        size = len(prices)
        if size < 2:
            return 0
        profit = 0
        buy = 0x7FFFFFFF
        sell = None
        for p in prices:
            if sell is None:
                if p > buy:
                    sell = p
                else:
                    buy = p
            else:
                if p < sell:
                    profit += sell - buy
                    buy = p
                    sell = None
                else:
                    sell = p
        if sell is not None:
            profit += sell - buy
        return profit