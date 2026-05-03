"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        hm = {}
        def traverseNode(node):
            newNode = Node(val = node.val)
            hm[node.val] = newNode
            for neighbor in node.neighbors:
                if neighbor.val not in hm:
                    traverseNode(neighbor)
                newNode.neighbors.append(hm[neighbor.val])
        traverseNode(node)
        return hm[node.val]
