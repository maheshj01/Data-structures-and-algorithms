# Problem 239 (Hard): https://leetcode.com/problems/sliding-window-maximum/
# time complexity: O(n)
# space complexity: O(k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,3,-1,-3,5,3,6,7], k = 3
        # [1,3,-1,-3,-10,3,6,7], k = 3
        # q = [1, ]
        # q = []
        # q = [3]
        # q = [-1, -3, -10]
        # result = [3, 3, -1]
        # left = 1, right = 3
        q = deque()
        left = 0
        result = []
        for right in range(len(nums)):
            while(q and q[-1] < nums[right]):
                q.pop()
            q.append(nums[right])
            if(right - left + 1 == k):
                max_element = q[0]
                result.append(max_element)
                # We have to ensure q[0] has top element from current window
                # if max on q does not belong to window pop it
                if(q[0] == nums[left]):
                    q.popleft()
                left += 1
        return result