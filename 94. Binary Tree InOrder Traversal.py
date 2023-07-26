# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr,TreeNode):
                res.append(curr)
                continue
            if curr.right is not None:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
        return res
