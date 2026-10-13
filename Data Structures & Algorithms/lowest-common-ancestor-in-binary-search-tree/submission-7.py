# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(curNode):
            if not curNode:
                return
            # if the value is between (or equal) to p and q, track it as result
            # the moment this isn't the case return back
            if (p.val >= curNode.val and q.val <= curNode.val) or (p.val <= curNode.val and q.val >= curNode.val): 
                # it stops here
                return curNode 

            # if both values are on the irght side explore that
            if (p.val >= curNode.val and q.val >= curNode.val):
                return dfs(curNode.right)
            else:
                return dfs(curNode.left)


        return dfs(root)