# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merging(root1,root2,dummy):
            if not root1 and not root2:
                return None
            if not root1 and root2:
                return root2
            if not root2 and root1:
                return root1

            dummy1 = TreeNode()
            dummy1.left = merging(root1.left, root2.left,dummy)
            dummy1.right = merging(root1.right, root2.right,dummy)
           
            dummy1.val = root1.val + root2.val

            return dummy1


        if not root1 and not root2:
            return None
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1

        dummy = TreeNode()

        return merging(root1,root2,dummy)
       

        

        


        