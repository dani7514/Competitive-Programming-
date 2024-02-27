# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def inorder(node, result):
            if node is None:
                return

            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

    
        result = []
        inorder(root, result)

        low_index = result.index(low)
       
        high_index = result.index(high)

        return sum(result[ low_index : high_index + 1])
