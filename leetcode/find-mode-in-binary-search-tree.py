# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]

        def inorder(node, result):
            if node is None:
                return

            if node.val in result:
                result[node.val] += 1
            else:
                result[node.val] = 1
            inorder(node.left, result)
            inorder(node.right, result)
        
        result = {}
        inorder(root, result)

        dicval_list = list(result.values()) 
        maxT = max(dicval_list) 

        res = []
        for i in result:
            if result[i] == maxT:
                res.append(i)

        return res



        