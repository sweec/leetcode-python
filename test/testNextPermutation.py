import unittest
from NextPermutation import Solution

class Test(unittest.TestCase):


    def testNextPermutation(self):
        s = Solution()
        nums = [[1,2,3], [3,2,1], [1,1,5], [1,2,4,3]]
        ans = [[1,3,2], [1,2,3], [1,5,1], [1,3,2,4]]
        for num, an in zip(nums, ans):
            self.assertEqual(s.nextPermutation(num), an)

if __name__ == "__main__":
    unittest.main()