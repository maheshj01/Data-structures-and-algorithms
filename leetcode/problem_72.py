### Problem 72. Edit Distance
### tags: Dynamic Programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #       h o r s e 
        #     0 1 2 3 4 5
        # r   1 1 2 2 3 4
        # o   2 2 1 3 4 5
        # s   3 3 4 5 3 6
    
    # if (match): dp = diagonal
    # else: min(left, top, diagonal) + 1
        col = len(word1)
        row = len(word2)
        dp = [[0] * (col + 1) for i in range(row+1)]
        # prefill first column
        for i in range(row + 1):
            dp[i][0] = i

        # prefill first row
        for j in range(col + 1):
            dp[0][j] = j
        
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if(word1[j - 1] == word2[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[row][col]

                    


        







