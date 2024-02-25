# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkSymmetry(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            left = checkSymmetry(p.left,q.right)
            right = checkSymmetry(p.right,q.left)

            return p.val == q.val and left and right

        return checkSymmetry(root.left, root.right)