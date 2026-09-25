# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        result = ListNode()
        temp = result

        if (n1 == None):
            return n2
        elif (n2 == None):
            return n1
        else:
            while (n1 != None and n2 != None):
                if n1.val < n2.val:
                    result.next = n1
                    n1 = n1.next
                else:
                    result.next = n2
                    n2 = n2.next
                result = result.next
            result.next = n1 or n2
            return temp.next
        