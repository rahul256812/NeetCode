# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
            
        # queue = deque([root])
        # depth = 0
        
        # while queue:
        #     level_size = len(queue)
            
        #     for _ in range(level_size):
        #         curr = queue.popleft()
                
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
            
        #     depth += 1
            
        # return depth
        
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)
        depth=max(left, right)+1

        return depth


