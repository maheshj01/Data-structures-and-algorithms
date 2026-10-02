class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        #  k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
        # min_capital = [(0, 1) ,(1, 2), (2, 3)]
        # max_profit = [(3, 1), (2, 1), (1, 0)]

        # if k not met or in budget
        # w = 1

        # for each project, can we pick a project?
        # which project to pick first
        # time complexity: O(n log n + k log n)
        min_heap_capital = [(capital[i], profits[i]) for i in range(len(capital))]
        max_heap_profit = []
        # O(n)
        heapq.heapify(min_heap_capital)

        while(k > 0):
            ## n(logn)
            while(min_heap_capital and min_heap_capital[0][0] <= w):
                c, p  = heapq.heappop(min_heap_capital)
                heapq.heappush(max_heap_profit, p * -1)
            if(not max_heap_profit):
                break
            # klog(n)
            profit = heapq.heappop(max_heap_profit)
            w -= profit
            k -= 1
        return w