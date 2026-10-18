# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        # brute force:
        # for each node determine the height of left vs right
        # if the difference is greater than 1 return false

        # otherwise wereturn true
        #O(N^2) since we traverse the tree for every node
        

        # for O(N) we want to combine traversing the tree for each node and also finding the height
        status = True

        def dfsGetHeight(curNode):
            if not curNode:
                return 0
            nonlocal status
            leftHeight = 0
            if curNode.left:
                leftHeight = dfsGetHeight(curNode.left)
            rightHeight = 0
            if curNode.right:
                rightHeight = dfsGetHeight(curNode.right)
            if abs(leftHeight - rightHeight) > 1:
                status = False
            
            # check if its balanced
            return max(leftHeight, rightHeight) + 1
        
        dfsGetHeight(root)
        return status