# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverseTree(ptr, upper, lower):
            if ptr == None:
                return True
            if ptr.val >= upper or ptr.val <= lower:
                return False
            return traverseTree(ptr.left, ptr.val, lower) and traverseTree(ptr.right, upper, ptr.val)
        return traverseTree(root, float('inf'), float('-inf'))