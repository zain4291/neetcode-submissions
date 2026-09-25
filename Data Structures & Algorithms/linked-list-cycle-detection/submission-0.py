# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = {}
        curr = head
        while curr:
            cycle[curr] = 1 + cycle.get(curr, 0)

            if curr.next in cycle:
                return True
            
            curr = curr.next
        return False