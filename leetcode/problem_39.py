### Problem 39. Combination Sum (Medium): https://leetcode.com/problems/combination-sum/
### tags: backtracking, recursion
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index, total, arr):
            if(index >= len(candidates) or total > target):
                return
            if(total == target):
                result.append(arr.copy())
                return

            arr.append(candidates[index])
            dfs(index, total + candidates[index], arr)
            arr.pop()
            dfs(index + 1, total, arr)

        dfs(0, 0, [])
        return result



# There is a pattern to solve this backtracking problem:
# 1. Add the current element to the combination
# 2. Recursively call the function with the next index and the updated total
# 3. Pop the current element from the combination
# 4. Recursively call the function with the next index and the updated total
# 5. Return the result

# This pattern is used to solve the problem of finding all combinations of a target sum using a list of candidates.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []
        def backtrack(index, total):
            if(total == target):
                result.append(combinations[:])
                return
            if(total > target):
                return
            
            for i in range(index, len(candidates)):
                combinations.append(candidates[i])
                backtrack(i, total + candidates[i])
                combinations.pop()
        
        backtrack(0, 0)
        return result
        # combinations = [2,2,2] : pop
        
        # [2, 2, 2, 2] : pop
        # [2, 2, 2] : 
        # [2, 2, 2, 3] : pop
        # [2, 2, 2]
        # [2, 2, 2, 6] : pop
        # [2, 2, 2]
        # [2, 2, 2, 7] : pop
        # [2, 2, 3] = target
        # [2, 2]
        # [2, 2, 6] pop 
        # [2, 2]
        # [2, 2, 7]: pop
        # [2, 3, 6]
        # [2, 3, 6]: pop
        # [2, 3]
        # [2, 3, 7]: pop
        # [2, 6]