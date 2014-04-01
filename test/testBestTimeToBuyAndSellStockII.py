import unittest
from BestTimeToBuyAndSellStockII import Solution

class Test(unittest.TestCase):


    def testMaxProfit(self):
        s = Solution()
        prices = [1, 2, 1, 3, 5]
        num = s.maxProfit(prices)
        self.assertEqual(num, 5, "max profit not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()