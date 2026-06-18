# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        before = head
        curr = head.next

        before.next = None
        while curr.next:
            after = curr.next
            curr.next = before
            before, curr = curr, after
        
        curr.next = before
        
        return curr
