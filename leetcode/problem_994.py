# Problem 994: Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_count = 0
        # bfs: At each minute a rotten orange can rot a fresh orange from all adjacent directions
        
        # rotten oranges only
        dq = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if(grid[row][col] == 1):
                    fresh_count += 1

                if(grid[row][col] == 2):
                    dq.append((row, col))
        
        # [(0,1), (1,0)]
        fresh = 1
        rotten = 2
        minutes = 0 
        while(dq and fresh_count > 0):
            size = len(dq)
            minutes += 1
            for x in range(size):
                row, col = dq.popleft()
                directions = [(0,1),(1,0),(0, -1),(-1, 0)]
                for r, c in directions:
                    pr, pc = row + r, col + c
                    isInBounds = (0 <= pr < len(grid)) and (0 <= pc < len(grid[0]))
                    if(isInBounds and grid[pr][pc] == fresh):
                        grid[pr][pc] = rotten
                        dq.append((pr, pc))
                        fresh_count -= 1
        if(fresh_count == 0):
            return minutes
        return -1
            
        



