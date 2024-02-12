# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur = head
        cur1 = head 

        while cur1 and cur1.next:
            cur = cur.next
            cur1 = cur1.next.next
            if cur == cur1:
                return True

        return False