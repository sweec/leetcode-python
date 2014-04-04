import unittest
from IntegerToRoman import Solution

class Test(unittest.TestCase):


    def testIntToRoman(self):
        s = Solution()
        ans = ['MCMXCVI', 'MMXIV', 'MLXVI']
        nums = [1996, 2014, 1066]
        romans = [s.intToRoman(num) for num in nums]
        self.assertEqual(romans, ans, "Roman number not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()