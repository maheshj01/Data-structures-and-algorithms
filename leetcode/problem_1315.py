# Problem 1315: Sum of Nodes with Even-Valued Grandparent
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # Iterative
        stack = [(root, None, None)]
        result = 0
        while(stack):
            top, parent, grandParent = stack.pop()
            if(top and grandParent and grandParent.val % 2 == 0):
                result += top.val
            if(top.left):
                stack.append((top.left, top, parent))
            if(top.right):
                stack.append((top.right, top, parent))
        return result


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        result = 0
        # [[6], [7, 8], [2, 7, 1, 3], [9, 1, ,4 ,5]]
        def dfs(node, parent, grandParent):
            nonlocal result
            if(not node):
                return
            if(grandParent and grandParent.val % 2 == 0):
                result += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
            
        dfs(root, None, None)
        return result