class Solution():
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        num = 0
        for n in A:
            num ^= n
        return num