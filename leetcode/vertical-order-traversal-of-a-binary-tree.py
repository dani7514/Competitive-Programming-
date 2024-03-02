# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = defaultdict(list)

        def DFS(node, row, col):
            if node is None:
                return
            data[col].append((row, node.val))
            DFS(node.left, row + 1, col - 1)
            DFS(node.right, row + 1, col + 1)

        DFS(root, 0, 0)

        
        data = dict(sorted(data.items()))
        for k in data.keys():
            data[k] = sorted(data[k], key=lambda e: (e[0], e[1]))

        ans = []
        for l in data.values():
            tmp = []
            for entry in l:
                tmp.append(entry[1])
            ans.append([x for x in tmp])

        return ans