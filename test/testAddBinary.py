import unittest
from AddBinary import Solution

class Test(unittest.TestCase):


    def testAddBinary(self):
        s = Solution()
        a = '1111'
        b = '1111'
        an = '11110'
        self.assertEqual(s.addBinary(a, b), an)

if __name__ == "__main__":
    unittest.main()