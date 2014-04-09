import unittest
from ValidParentheses import Solution

class Test(unittest.TestCase):


    def testIsValid(self):
        s = Solution()
        strs = ["[", "()", "()[]{}", "(]", "([)]"]
        ans = [False, True, True, False, False]
        for S, an in zip(strs, ans):
            self.assertEqual(s.isValid(S), an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()