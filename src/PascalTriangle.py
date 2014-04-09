class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        cureRow = [1]
        for i in range(rowIndex):
            nextRow = [1]
            for j in range(i):
                nextRow.append(cureRow[j]+cureRow[j+1])
            nextRow.append(1)
            cureRow = nextRow
        return cureRow