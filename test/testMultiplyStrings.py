import unittest
from MultiplyStrings import Solution

class Test(unittest.TestCase):


    def testMultiply(self):
        s = Solution()
        num1 = '123456'
        num2 = '123345'
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()