class Solution:
    # @return an integer
    def numTrees(self, n):
        if n < 1:
            return 0
        nums = [1]
        for i in range(1, n+1):
            num = 0
            for j in range(0, i/2):
                num += nums[j] * nums[i-1-j]
            num += num
            if i&1 == 1:
                num += nums[(i-1)/2] * nums[(i-1)/2]
            nums += [num]
        return nums[n]