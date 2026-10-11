# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([root])

        while queue:
            qlen = len(queue)
            trip = []

            for i in range(qlen):
                node = queue.popleft()
                if node:
                    trip.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if trip:
                res.append(trip)
        return res