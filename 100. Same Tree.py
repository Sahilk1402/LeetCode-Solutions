# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p == q:
            return True
        try:
            left = right = True
            if p.val == q.val:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right,q.right)
                return (left and right)
        except:
            return False
        return False
