# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # O(N)

        def dfs(curNode, minVal, maxVal):
            if not curNode:
                return True
            
            val = curNode.val
            if val <= minVal or val >= maxVal:
                return False
            
            if curNode.left and not dfs(curNode.left, minVal, min(curNode.val, maxVal)):
                return False
            if curNode.right and not dfs(curNode.right, max(minVal, curNode.val), maxVal):
                return False
                
            
            return True
        return dfs(root, -float('inf'), float('inf'))