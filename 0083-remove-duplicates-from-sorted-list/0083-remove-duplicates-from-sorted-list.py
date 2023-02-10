# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr:
            next = curr.next
            while next and next.val == curr.val:
                next = next.next

            curr.next = next
            curr = curr.next

        return head
        