# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # left to right level and level 
        

        # bfs

        # how high is this thing??
        res = []

        # one pass

        # use bfs to traverse the thing level by level
        # always add left most first
        q = deque()
        if root:
            q.append((0,root))

        while q:
            level,node = q.popleft()
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            # look for left most add it, look for right mostadd it
            if node.left:
                q.append((level + 1,node.left))
            if node.right:
                q.append((level + 1,node.right))
        
        return res