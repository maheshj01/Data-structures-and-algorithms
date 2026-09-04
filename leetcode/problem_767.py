# Problem 767. Reorganize String
# tags: heap, string
class Solution:
    def reorganizeString(self, s: str) -> str:
        # abccabbd
        
        # a: 2
        # b: 3
        # c: 2
        # d: 1
        freq = Counter(s)
        print(freq)
        heap = []
        max_f = -1
        for k, v in freq.items():
            heap.append((-v, k))
            max_f = max(max_f,v)
        if max_f > (len(s) + 1) // 2:
            return ""
            
        heapify(heap)
        print(heap)
        res = []
        prev_k = ""
        prev_v = 0
        while(heap):
            # [(-2, 'a'), (-2, 'c'), (-1, 'd')]
            v, k = heapq.heappop(heap)
            # [(-1, 'a'), (-2, 'c'), (-1, 'd')]
            res.append(k)
            if(prev_v != 0):
                heapq.heappush(heap, (prev_v, prev_k))
                # [(-2, 'b'), (-2, 'c'),(-1, 'a'), (-1, 'd')]
            prev_v = v + 1
            prev_k = k

        return ''.join(res)
