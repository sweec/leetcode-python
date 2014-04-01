import unittest
from ReverseInteger import Solution

class Test(unittest.TestCase):


    def testSingleNumber(self):
        s = Solution()
        xs = [12, -12, 0]
        ans = [21, -21, 0]
        for x, an in zip(xs, ans):
            num = s.reverse(x)
            self.assertEqual(num, an, "reverse value not agree")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()