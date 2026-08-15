# Problem 1208 (Medium): https://leetcode.com/problems/get-equal-substrings-within-budget/
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #  s = "abcd", t = "bcdf", maxCost = 3
        # [1, 1, 1, 2]
        costs = []
        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            cost = abs(ord(letter_s) - ord(letter_t)) 
            costs.append(cost)
        print("costs=", costs)

        # [1, 1, 1, 2], maxCost = 3
        # [1]
        # costs= [15, 8, 6, 12, 4],  maxCost = 19
        
        left = 0
        curr_sum = 0
        max_len = 0
        for right in range(len(costs)):
            curr_sum += costs[right]
            while(curr_sum > maxCost):
                curr_sum -= costs[left]
                left += 1
                    
            curr_win_len = right - left + 1
            max_len = max(max_len, curr_win_len)
        return max_len


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        curr_sum = 0
        max_len = 0
        for right in range(len(s)):
            cost_right = abs(ord(s[right]) - ord(t[right])) 
            curr_sum += cost_right
            while(curr_sum > maxCost):
                cost_left = abs(ord(s[left]) - ord(t[left])) 
                curr_sum -= cost_left
                left += 1
            curr_win_len = right - left + 1
            max_len = max(max_len, curr_win_len)
        return max_len


