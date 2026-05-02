# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        larger, smaller = (p.val, q.val) if (p.val > q.val) else (q.val, p.val)
        while root != None:
            if root.val <= larger and root.val >= smaller:
                return root
            elif root.val <= larger and root.val <=smaller:
                root = root.right
            else:
                root = root.left
