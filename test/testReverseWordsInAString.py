import unittest
from ReverseWordsInAString import Solution

class Test(unittest.TestCase):


    def testReverseWords(self):
        s = Solution()
        sentence = 'the sky is blue  '
        self.assertEqual(s.reverseWords(sentence), "blue is sky the")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSingleNumber']
    unittest.main()