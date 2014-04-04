import unittest
from RomanToInteger import Solution

class Test(unittest.TestCase):


    def testRomanToInt(self):
        s = Solution()
        romans = ['MCMXCVI', 'MMXIV', 'MLXVI']
        ans = [1996, 2014, 1066]
        nums = [s.romanToInt(roman) for roman in romans]
        self.assertEqual(nums, ans, "number not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()