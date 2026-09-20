
### 787. Cheapest Flights Within K Stops
### tags: graphs, bfs, dijkstra's


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # tuple will hold travelled_cost, current Node, stops
        # heap = [, (700, 3, 2)]
        # travelled_cost = 200,
        # node = 2,
        # stops = 2
        # target = 3
        # 
        # adjacent list
        adj = defaultdict(list)
        for fromi, toi, pricei in flights:
            adj[fromi].append((pricei, toi))
        print("adj = ", adj)

        # (travelled_cost, current Node, stops)
        heap = [(0, src, -1)]
        visited = set()
        while(heap):
            travelled_cost, node, stops = heapq.heappop(heap)
            if((node, stops) in visited):
                continue
            visited.add((node, stops))
            if(node == dst):
                return travelled_cost
            if(stops == k):
                continue
            for price, neighbor, in adj[node]:
                if (neighbor, stops + 1) not in visited:
                    heapq.heappush(heap, (travelled_cost + price, neighbor, stops + 1))
        return -1