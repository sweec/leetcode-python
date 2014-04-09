class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows:
            return []
        preRow = [1]
        A = [preRow]
        for i in range(numRows-1):
            curRow = [1]
            for j in range(i):
                curRow.append(preRow[j]+preRow[j+1])
            curRow.append(1)
            A.append(curRow)
            preRow = curRow
        return A