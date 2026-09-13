### Problem 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        # x: input amount of cash when entering house at x
        # f(x): amount of cash after robbing the house x

        # f(1) = 1
        # f(2) = max(f(2), f(1)),
        # f(3) = max(f(1) + nums[3], f(2))
        # f(4) = max(f(2) + nums[4], f(3))
        
        if(len(nums) == 1):
            return nums[0]
        x = nums[0]
        y = max(nums[0], nums[1])
    
        # dp: = [1, 2, 0, 0, 0]
        for i in range(2, len(nums)):
            z = max(x + nums[i], y)
            x = y
            y = z
        return y