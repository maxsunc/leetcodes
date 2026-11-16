class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # rots adjacent oranges
        # Keep track of all the rotten oranges
        # Multi source bfs on each
        n, m = len(grid), len(grid[0])

        q = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 2:
                    q.append(((i,j),0)) # rotten position, at time 0
        res = 0
        while q:
            entry = q.popleft()
            res = max(res, entry[1])
            i,j = entry[0]
            # rot around us
            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]
                if 0 <= newI and newI < n and newJ >= 0 and newJ < m and grid[newI][newJ] == 1:
                    grid[newI][newJ] = 2
                    newEntry = ((newI,newJ), entry[1] + 1)
                    q.append(newEntry)
        
        # print(grid)
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    return -1
        return res