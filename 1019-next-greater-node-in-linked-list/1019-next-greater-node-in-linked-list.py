# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
            if not head:
                return None
            values = []
            while head:
                values.append(head.val)
                head = head.next        
            stack = []
            res = [0] * len(values)
            for idx, v in enumerate(values):
                while stack and v > stack[-1][-1]:
                    res[stack[-1][0]] = v
                    stack.pop()
                stack.append([idx, v])
            return res
        