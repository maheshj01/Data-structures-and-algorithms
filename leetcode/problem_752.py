class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
         
        #  LEVEL 0    LEVEL 1    LEVEL 2    LEVEL 3
        #  0 0 0 0    0 0 0 1    0 0 0 1    1 0 0 0    
        #             0 0 1 0    0 0 2 0     
        #             0 1 0 0    
        #             1 0 0 0    
        #             9 0 0 0    
        #             0 9 0 0    
        #             0 0 9 0    
        #             0 0 0 9    

        def neighbours(pattern):
            result = []
            # arr = [int(x) for x in pattern.split()]
            for i in range(len(pattern)):
                x = (int(pattern[i]) + 1) % 10
                y = (int(pattern[i]) - 1) % 10
                result.append(pattern[:i] + str(x) + pattern[i+1 :])
                result.append(pattern[:i] + str(y) + pattern[i+1 :])
            return result

        deadEnds = set(deadends)
        if('0000' in deadEnds):
            return -1
        visited = {'0000'}
        q = deque([('0000', 0)])
        while(q):
            pattern, level = q.popleft()
            if(pattern == target):
                return level
            nbrs = neighbours(pattern)
            for nbr in nbrs:
                if((nbr not in visited) and (nbr not in deadEnds)):
                    q.append((nbr, level + 1))
                    visited.add(nbr)
        return -1    
