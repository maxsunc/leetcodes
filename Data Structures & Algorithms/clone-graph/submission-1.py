"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # find a deep copy of the graph

        # each graph node must be copied over

        nodeToCopy = {}

        # first pass: make copies of all the nodes
        # 2nd pass: connect up the copies (copy over the neighboring data) since all copies of each nodes are already made
        def dfsCopyFirstPass(curNode):
            if not curNode:
                return
            if curNode in nodeToCopy:
                return
            nodeToCopy[curNode] = Node(curNode.val,[])
            # explore all neighbors
            for n in curNode.neighbors:
                dfsCopyFirstPass(n)
        seen = set()
        def dfsWireUp(curNode):
            if not curNode:
                return
            if curNode in seen:
                return
            seen.add(curNode)
            for n in curNode.neighbors:
                # print(nodeToCopy[n])
                nodeToCopy[curNode].neighbors.append(nodeToCopy[n])
                dfsWireUp(n)
        dfsCopyFirstPass(node)
        # print(nodeToCopy)
        dfsWireUp(node)
        return nodeToCopy[node] if node is not None else None