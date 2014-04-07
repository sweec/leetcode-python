import unittest
from GenerateParentheses import Solution

class Test(unittest.TestCase):


    def testGenerateParentheses(self):
        s = Solution()
        an = ["()()()", "(())()", "()(())", "(()())", "((()))"]
        self.assertEqual(s.generateParenthesis(3), an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()