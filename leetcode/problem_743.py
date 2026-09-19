### tags: 743. Network Delay
### tags: Dijsktra's , graphs, heap, bfs

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    
        adj = {}
        result = 0
        for times in times:
            if(times[0] not in adj):
                adj[times[0]] = []
            adj[times[0]].append((times[1], times[2]))
        print(adj)
        heap = [(0, k)]
        visited = set()
        while(heap):
            time, node = heapq.heappop(heap)
            visited.add(node)
            if(len(visited) == n):
                return time
            for neighbor, wt in adj.get(node, []):
                if(neighbor not in visited):
                    heapq.heappush(heap, (wt + time, neighbor))
        return -1