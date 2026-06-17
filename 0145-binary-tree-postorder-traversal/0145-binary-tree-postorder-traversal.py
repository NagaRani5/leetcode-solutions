# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def postorder(node):
            if not node:
                return 
            else:
                postorder(node.left)
                postorder(node.right)
                r.append(node.val)
        postorder(root)
        return r
    
        