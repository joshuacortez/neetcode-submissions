# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        # when fast is at n, then it is L-n away from the end
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        slow.next = None
        return head