class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        target = image[sr][sc]
        seen = set()

        def dfs(i,j):
            if (i,j) in seen:
                return
            
            # set this color to dude
            image[i][j] = color
            seen.add((i,j))

            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]

                if 0 <= newI < len(image) and 0 <= newJ < len(image[0]) and image[newI][newJ] == target:
                    dfs(newI,newJ)
            
        
        dfs(sr,sc)

        return image