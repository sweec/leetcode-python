import unittest
from AllUniqueCharactersInString import Solution

class Test(unittest.TestCase):


    def testIsAllUnique(self):
        s = Solution()
        As = ['abcd1234a', 'abcd1234']
        ans = [False, True]
        for A, an in zip(As, ans):
            self.assertEqual(s.isAllUnique(A), an)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()