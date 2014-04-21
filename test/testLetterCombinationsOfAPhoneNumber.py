import unittest
from LetterCombinationsOfAPhoneNumber import Solution

class Test(unittest.TestCase):


    def testLetterCombinations(self):
        s = Solution()
        digits = "23"
        an = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        A = s.letterCombinations(digits)
        self.assertEqual(len(A), len(an))
        for a in A:
            self.assertTrue(a in an)

if __name__ == "__main__":
    unittest.main()