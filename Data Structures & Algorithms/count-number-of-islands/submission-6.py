class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # counting the number of islands in a grid:
        # islands is bodies of 1s connected left irght up and down, not diagonal
        seen = set()
        res = 0
        def dfsExplore(i,j):
            if (i,j) in seen or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            # visit this area, asume it is a 1
            seen.add((i,j))

            dfsExplore(i + 1, j)
            dfsExplore(i-1, j)
            dfsExplore(i, j +1)
            dfsExplore(i,j-1)

        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # print(f"checked {(i,j)}")
                if grid[i][j] == "1" and not ((i,j) in seen):
                    res += 1
                    dfsExplore(i,j)
                    # print(f"{seen} after {res}")
        return res