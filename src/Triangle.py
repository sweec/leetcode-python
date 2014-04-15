class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        curRow = [0]
        for row in triangle:
            nextRow = []
            for i, n in enumerate(row):
                if i == 0:
                    nextRow.append(n+curRow[0])
                elif i == len(row)-1:
                    nextRow.append(n+curRow[-1])
                else:
                    nextRow.append(n+min(curRow[i-1], curRow[i]))
            curRow = nextRow
        return min(curRow)