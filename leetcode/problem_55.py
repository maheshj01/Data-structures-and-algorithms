# Problem 55. Jump Game (Medium): https://leetcode.com/problems/jump-game/

# hint: uses greedy approach by trying to reach a index lower every time
# if we reach at the beginning, then we can jump until the end of the array
# Time: O(n), Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1;
        current = lastIndex - 1
        while(current >= 0):
            if(nums[current] + current >= lastIndex):
                lastIndex = current
            current -= 1
        if(lastIndex == 0):
            return True
        else:
            return False

class Solution2:
    def canJump(self, nums: list[int]) -> bool:
        # [2,3,1,1,4]
        # f(x) = x
        # [3,3,1,0,4]
        # reach = (reach + nums[i])
        reach = 0
        for i in range(len(nums)):
            if(i > reach):
                return False
            reach = max(reach, i + nums[i])
            if(reach >= len(nums) - 1):
                return True
        return False

# Alternate solution: Take the jump that is greater than current jump

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums)) # True
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums)) # False
    nums = [2,0,0]
    print(Solution().canJump(nums)) # True
    nums = [0]
    print(Solution().canJump(nums)) # True