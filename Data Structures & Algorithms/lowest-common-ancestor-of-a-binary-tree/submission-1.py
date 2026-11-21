# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find the LCA of two nodes
        # is it on the left and right
        # if both is on the left: go to left
        result = (root,0)

        def dfs(curNode, level):
            nonlocal result
            res = [False, False]
            if curNode == p:
                res[0] = True
            if curNode == q:
                res[1] = True
            val1, val2 = [False,False],[False,False]
            if curNode.left:
                val1 = dfs(curNode.left, level + 1)
            if curNode.right:
                val2 = dfs(curNode.right, level + 1)

            res = [res[0] or val1[0] or val2[0], res[1] or val1[1] or val2[1]]

            if res[0] and res[1] and level > result[1]:
                result = (curNode, level)

            return res
        dfs(root, 0)
        return result[0]