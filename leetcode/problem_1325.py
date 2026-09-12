### Problem 1325. Delete Leaves With a Given Value
### tags: tree, dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if(not root):
                return None
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            # if(not left and not right and root.val == target):
            if(not root.left and not root.right and root.val == target):
                return None
            return root  