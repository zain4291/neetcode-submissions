# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p:
            return False
        if not q:
            return False

        if p.val == q.val:
            t1 = self.isSameTree(p.left, q.left)
            t2 = self.isSameTree(p.right, q.right)

            return t1 and t2
        return False