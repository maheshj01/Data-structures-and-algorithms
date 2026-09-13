### Problem 1143. class Solution:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #     a  c e 
        # a | 1  1 1
        # b | 1  1 1
        # c | 1  2 2
        # d | 1  2 2
        # e | 1  2 3

        #     a  c  d e 
        # a | 1  1  1 1 
        # b | 1  1  1 1
        # c | 1  2  2 2
        # d | 1  2  3 3
        # e | 1  2  3 4

        # if(match): dp[i][j] = dp[i-1][j-1] + 1
        # else: dp[i-1][j-1]
        m = len(text1)
        n = len(text2)
        prev = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n+1):
                if(text1[i - 1] == text2[j - 1]):
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev = curr
        return prev[n]

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp =[[0]* (n + 1) for i in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if(text1[i - 1] == text2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]