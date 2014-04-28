import unittest
from EditDistance import Solution

class Test(unittest.TestCase):


    def testEditDistance(self):
        s = Solution()
        word1 = 'abc'
        word2 = 'ef'
        self.assertEqual(s.minDistance(word1, word2), 3)

if __name__ == "__main__":
    unittest.main()