# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max1=0
        def DFS(root):
            if root is None:
                return 0,inf,-inf,True

            left= DFS(root.left)
            right=DFS(root.right)

            if (left[3] and right[3]) and (left[2]<root.val and root.val<right[1]):
                sum1=root.val+left[0]+right[0]
                nonlocal max1
                max1=max(max1,sum1)
            else:
                return 0,0,0,False
            
            return sum1,min(root.val,left[1]),max(root.val,right[2]),True

        DFS(root)
        return max1