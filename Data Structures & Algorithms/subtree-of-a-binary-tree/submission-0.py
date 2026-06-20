# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it cannot contain a non-empty subtree
        if not root:
            return False
        
        # Check if the trees match starting at the current root
        if self.isSameTree(root, subRoot):
            return True
        
        # If they don't match, look for the subtree in the left or right children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are null, so they are identical
        if not p and not q:
            return True
        
        # One is null and the other isn't, or their values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)