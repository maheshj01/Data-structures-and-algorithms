### Problem 112. Path Sum
### Tags: Tree, Depth First Search, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPath(root,targetSum):
            if(root is None):
                return False
            else:
                targetSum -= root.val
                if(root.left is None and root.right is None):
                    return targetSum == 0
                return hasPath(root.left, targetSum) or hasPath(root.right, targetSum)
        return hasPath(root, targetSum)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def dfs(node, sum):
            if(not node):
                return False
            sum += node.val
            if(not node.left and not node.right and sum == targetSum):
                return True
            left = dfs(node.left, sum)
            right = dfs(node.right, sum)
            if(left or right):
                return True
            return False
        
        return dfs(root, 0)