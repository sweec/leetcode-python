import unittest
from PalindromeNumber import Solution

class Test(unittest.TestCase):


    def testIsPalindrome(self):
        s = Solution()
        xs = [121, -5, 0, 134, 120030221]
        ans = [True, False, True, False, False]
        for x,an in zip(xs, ans):
            self.assertEqual(s.isPalindrome(x), an)

if __name__ == "__main__":
    unittest.main()