# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        cur = slow
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp
            
        slow = prev

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True