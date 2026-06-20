# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the midpoint 
        # reverse the 2nd half
        # merge the two linked lists

        if not head or not head.next:
            return

        # fid the midpoint first
        slow = head
        fast = head.next
        while True:
            slow = slow.next
            fast = fast.next.next

            if not fast:
                is_odd = True
                break

            if not fast.next:
                is_odd = False 
                break
        mid = slow
        
        # then reverse the 2nd half
        prev = None
        curr = mid.next
        while curr:
            after = curr.next
            curr.next = prev
            prev, curr = curr, after
        tail = prev

        # then merge the two linked lists
        dummy = ListNode()

        merged = dummy
        curr1 = head
        curr2 = tail
        while curr2:
            if curr1:
                merged.next = curr1
                merged = merged.next
                curr1 = curr1.next
            if curr2:
                merged.next = curr2
                merged = merged.next
                curr2 = curr2.next
        
        if is_odd:
            mid.next = None
            merged.next = mid

        head = dummy.next