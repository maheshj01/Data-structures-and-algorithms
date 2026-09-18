#### Problem 463

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        perimeter = 0
        def bfs(i, j):
            nonlocal perimeter
            if((i,j) in visited):
                return 
            visited.add((i, j))
            # left out of bounds or water
            if(j - 1 < 0 or grid[i][j - 1] == 0):
                perimeter += 1
            # right out of bounds or water
            if(j + 1 >= len(grid[0]) or (grid[i][j + 1] == 0)):
                perimeter += 1
            # top out of bounds or water
            if(i - 1 < 0 or (grid[i - 1][j] == 0)):
                perimeter += 1
            # bottom out of bounds or water
            if(i + 1 >= len(grid) or (grid[i + 1][j] == 0)):
                perimeter += 1
            
            # land on left
            if((j - 1) > 0 and grid[i][j - 1] == 1):
                bfs(i, j - 1)
            # land on right
            if((j + 1) < len(grid[0]) - 1 and grid[i][j + 1] == 1):
                bfs(i, j + 1)
            # land on top
            if((i - 1) > 0 and (grid[i - 1][j] == 1)):
                bfs(i - 1, j)
            # land on bottom
            if((i + 1) < len(grid) - 1 and (grid[i + 1][j] == 1)):
                bfs(i + 1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    bfs(i,j)
        
        return perimeter
