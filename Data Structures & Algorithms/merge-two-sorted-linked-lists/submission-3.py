# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2:
            if list1.val <= list2.val:
                head = ListNode(list1.val)

                curr1 = list1.next
                curr2 = list2
            else:
                head = ListNode(list2.val)
    
                curr1 = list1
                curr2 = list2.next
        elif list1 and not list2:
            return list1
        else:
            return list2

        body = head

        while curr1 or curr2:
            if curr1 and curr2:
                next_curr1 = curr1.next
                next_curr2 = curr2.next

                if curr1.val <= curr2.val:
                    body.next = ListNode(curr1.val)
                    curr1 = next_curr1
                else:
                    body.next = ListNode(curr2.val)
                    curr2 = next_curr2

                body = body.next

            elif curr1 and not curr2:
                body.next = curr1
                break
            else:
                body.next = curr2
                break

        return head 
                    