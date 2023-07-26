# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.preorderTraversalHelper(root)
        return self.res

    
    def preorderTraversalHelper(self,node):
        if node is None:
            return
        self.res.append(node.val)
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
