# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        maxwidth = 0
        while q:
            res = []
            for i in range(len(q)):
                node, num = q.popleft()
                res.append(num)
                if node.left:
                    q.append((node.left, num*2+1))
                if node.right:
                    q.append((node.right, num*2+2))
            maxwidth = max(maxwidth, res[-1] - res[0] + 1)
        return maxwidth