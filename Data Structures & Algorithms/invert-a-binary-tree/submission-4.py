# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # sqwap the right and left recursively


        def dfsSwap(curNode):
            if not curNode:
                return
            
            left = curNode.left
            curNode.left = curNode.right
            curNode.right = left
            dfsSwap(curNode.right)
            dfsSwap(curNode.left)
        dfsSwap(root)
        return root