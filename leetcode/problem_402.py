### Problem 402. Remove K Digits (Medium): https://leetcode.com/problems/remove-k-digits/
### Tags: Stack, Greedy, Monotonic Stack

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Input: num = "1 4 3 2 2 1 9", k = 3
        # "1, 0" = 2
        # [0]
        stack = []
        # [1, 2, 2, 1, 9 ] k = 3
        # k = 1, top = -, cur = 0
        for n in num:
            while(stack and int(stack[-1]) > int(n) and k > 0):
                stack.pop()
                k -= 1
            stack.append(n)
        while(k > 0):
            stack.pop()
            k -= 1
        index = 0
        while(index < len(stack) and stack[index] == '0'):
            index += 1
        result = "".join(stack[index:])
        return result if result else "0"