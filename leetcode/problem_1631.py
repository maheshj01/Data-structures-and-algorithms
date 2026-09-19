### 1631. Path With Minimum Effort
### tags: Dijsktra's , graphs, heap, bfs

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        
        heap = [(0, 0, 0)]
        visited = set()
        while(heap):
            distance, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if(i == len(heights) - 1 and j == len(heights[0]) - 1):
                return distance
            directions = [ (0,-1), (0, 1), (-1, 0), (1, 0)]
            for r, c in directions:
                nr = r + i
                nc = c + j                
                if(nr >= 0 and nr <= len(heights) - 1 and 
                    nc >= 0 and nc <= len(heights[0]) - 1):
                    if((nr, nc) not in visited):
                        diff = abs(heights[i][j] - heights[nr][nc])
                        heapq.heappush(heap, (max(diff, distance), nr, nc))

