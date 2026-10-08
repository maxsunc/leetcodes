# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummyNode = ListNode()
        curNode = dummyNode

        while list1 and list2:
            # grab the minimium of the two
            if list1.val > list2.val:
                curNode.next = ListNode(list2.val)
                list2 = list2.next
            else:
                curNode.next = ListNode(list1.val)
                list1 = list1.next
            curNode = curNode.next
        while list1:
            curNode.next = ListNode(list1.val)
            list1 = list1.next
            curNode = curNode.next
        
        while list2:
            curNode.next = ListNode(list2.val)
            list2 = list2.next
            curNode = curNode.next
        return dummyNode.next
