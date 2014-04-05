class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        index = 0
        hasDup = None
        for num in A:
            if num != A[index]:
                index += 1
                if hasDup:
                    A[index] = num
            elif not hasDup:
                if hasDup is None:
                    hasDup = False
                else:
                    hasDup = True
        return index+1