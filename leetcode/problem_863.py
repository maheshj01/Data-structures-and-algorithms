# Problem 863: All Nodes Distance K in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # [[5], [3, 6, 2], [7, 4, 1], [0, 8]]
        # 
        # hash map to store parents of a node
        map = {}
        def dfs(node, parent):
            if(not node):
                return
            map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        # print(map)
        dq = deque([(target, 0)])
        # if(targetRoot):
        #     print("target Root=", targetRoot.val)
        #     dq.append()
        visited = set({target})
        result = []
        # dq = [(8, 3)]
        # top = (0, 3)
        # target = 5
        # result = [1, 7, 4]
        # visited = (5, 3, 6, 2, 1, 7, 4, 0, 8)
        while(dq):
            top, level = dq.popleft()
            if(level == k):
                result.append(top.val)
                # if you have already reached a distance you don't need to check next level
                continue
            for x in [map[top], top.left, top.right]:
                if(x and x not in visited):
                    dq.append((x, level + 1))
                    visited.add(x)
        return result
