# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumN(node, result,s):
            if node is None:
                return

            s += str(node.val)
            if not node.left  and not node.right:
                result.append(s)
            
            sumN(node.left, result, s) 
            sumN(node.right, result, s)
            s = s[:-1]

    
        result = []
        s = ''
        sumN(root, result,s)
        
        res = 0
        for i in result:
            res += int(i) 

        return res
        