### Problem 62. Unique Paths
### tags: Dynamic Programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # f(0, 0): 2
        # f(0, 1): f(0, 0) + 
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

