# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # find the number of good nodes in a binary tree
        # from the path of root to node X there are no nodes with value greater than X
        # root here means the top vlaue right?
        # what if its equal?

        # return the number of good nodes
        # just an int
        if not root:
            return 0

        # do we include the root?
        # root itself is also one

        # Approach 1: dfs track the current maximum seen:
        # as the traverse the tree: If we see any values bigger than or equal the maximum that is a good node: set the new maximum
        # any values less the max are not good nodes
        # O(N) time complexity
        # O(N) worst case: recursion space complexity
        res = 0
        def dfs(curNode, maximum):
            nonlocal res
            if not curNode:
                return

            if curNode.val >= maximum:
                res += 1
                maximum = curNode.val
            # explore both sides
            dfs(curNode.left, maximum)
            dfs(curNode.right, maximum)
        dfs(root, root.val)
        return res
