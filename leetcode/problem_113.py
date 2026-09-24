### Problem 113. Path Sum II
# tags: trees, dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        
        # dfs(5, 5, [5])
        # dfs(4, 9,[5, 4])
        # dfs(11, 20, [5, 4, 11])
        # dfs(7, 27, [5, 4, 11, 7]) > 22
        # dfs(2,[5, 4, 11, 2]) == 2 add to result
        # dfs(11,[5, 4, 11])
        # dfs(4,[5, 4])
        # dfs(8,[5,8])
        # dfs(13,[5,8, 13])
        result = []
        def dfs(node, curr_sum, path):
            nonlocal result
            if(not node):
                return
            curr_sum += node.val
            new_path = path.copy()
            new_path.append(node.val)
            if(not node.left and not node.right and curr_sum == targetSum):
                result.append(new_path)
            
            dfs(node.left, curr_sum, new_path)
            dfs(node.right, curr_sum, new_path)
        
        dfs(root, 0, [])
        return result