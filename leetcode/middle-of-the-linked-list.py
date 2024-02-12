# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 1

        while cur.next:
            cur = cur.next
            length += 1

        middle = length // 2
 
        cur1 = head
        for i in range(middle):
            cur1 = cur1.next

        return cur1
