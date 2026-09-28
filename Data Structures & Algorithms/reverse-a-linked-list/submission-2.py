# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # recursive solution
        prev, cur = None, head
        def reverse():
            nonlocal cur
            nonlocal prev
            if not cur:
                return

            # point cur to prev and move to cur next and cur
            next = cur.next
            cur.next = prev
            # update prev and cur
            prev = cur
            cur = next

            reverse()
        reverse()
        return prev
