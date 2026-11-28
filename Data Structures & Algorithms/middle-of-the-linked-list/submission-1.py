# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # get the length

        # do ceil(length) thats ur node to get
        length = 0
        curNode = head
        while curNode != None:
            curNode = curNode.next
            length += 1
        
        curNode = head
        for i in range(0, length // 2):
            curNode = curNode.next
        
        return curNode