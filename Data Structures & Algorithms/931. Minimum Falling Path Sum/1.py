class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        # brute force:
        # bfs

        # dp: bottom up is easier to visualize here
        # create another matrix same size
        n = len(matrix)
        # is it possible ot have negative

        minVals = [[]for i in range(0,n)]

        def isValid(i,j):
            return 0 <= i < n and 0 <= j < n

        for i in range(n-1, -1, -1):
            for j in range(0, n):
                # see if i + 1,j,j-1,j+1 is in range
                if i + 1 >= n:
                    minVals[i].append(matrix[i][j])
                    continue
                minCandidate = minVals[i + 1][j]
                for offset in range(-1, 2):
                    if isValid(i + 1, j + offset):
                        minCandidate = min(minCandidate, minVals[i + 1][offset + j])
                minVals[i].append(minCandidate + matrix[i][j])
        

        # grab the max from the top row
        res = minVals[0][0]
        print(minVals)
        for i in range(0, n):
            res = min(res,minVals[0][i])
        return res
