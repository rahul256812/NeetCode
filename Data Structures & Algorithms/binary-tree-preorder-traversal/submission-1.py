class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            curr = curr.right
            
        return result