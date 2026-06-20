# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of linked list as L
        # remove L - n + 1th element
        # means we call .next L-n times

        L = 0
        curr = head
        while curr:
            L+=1
            curr = curr.next


        steps_away = L - n 
        if not steps_away:
            return head.next

        curr = head
        for i in range(steps_away):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr.next = None
        return head