# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = {}
        cur = head
        while cur:
            cycle[cur] = 1 + cycle.get(i, 0)

            if cur.next in cycle:
                return True
            cur = cur.next
        return False