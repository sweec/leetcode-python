class Solution():
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones, twos, threes = 0, 0, 0
        for n in A:
            twos |= ones & n
            ones ^= n
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones