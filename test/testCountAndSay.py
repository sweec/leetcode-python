import unittest
from CountAndSay import Solution

class Test(unittest.TestCase):


    def testCountAndSay(self):
        s = Solution()
        ns = range(1, 6)
        ans = ['1', '11', '21', '1211', '111221']
        for n, an in zip(ns, ans):
            self.assertEqual(s.countAndSay(n), an)

if __name__ == "__main__":
    unittest.main()