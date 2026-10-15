class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # bfs:
        # multi source bfs

        # bfs from each 1 is to slow since we're doing bfs for each 1 that exists
        # bfs on 0s, faster since each find of a 1 is the most optimal, so this is just one sweep

        queue = deque()

        n,m = len(mat), len(mat[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def isValid(i,j):
            return 0 <= i < n and 0 <= j < m

        res = [[-1 for j in range(0, m)] for i in range(0,n)]

        for i in range(0,n):
            for j in range(0,m):
                if mat[i][j] == 0:
                    entry = (i,j, 0)
                    queue.append(entry)
                    res[i][j] = 0
        
        while queue:
            entry = queue.popleft()
            i,j = entry[0], entry[1]
            dist = entry[2]
            # explore all around this current pos
            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]

                if isValid(newI,newJ) and res[newI][newJ] == -1:
                    newEntry = (newI,newJ, dist + 1)
                    res[newI][newJ] = dist + 1
                    # mark it as seen
                    # add it to queue
                    queue.append(newEntry)

        return res