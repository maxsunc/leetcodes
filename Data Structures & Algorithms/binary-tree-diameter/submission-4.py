# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get the height of left, height of right
        # 

        res = 0


        def dfsGetHeight(curNode):
            nonlocal res
            if not curNode:
                return 0
            
            leftHeight = dfsGetHeight(curNode.left) + 1
            rightHeight = dfsGetHeight(curNode.right) + 1
            res = max(res, leftHeight + rightHeight - 2)


            return max(leftHeight, rightHeight)


        dfsGetHeight(root)
        return res