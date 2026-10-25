# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # determine if there is a cycle in the linkedlist

        # keep track of the seen nodes
        # if its seen in there we return true, if we get to the end ret false
        seen = set()

        curNode = head

        while curNode:
            if curNode in seen:
                return True
            seen.add(curNode)

            curNode = curNode.next
        return False