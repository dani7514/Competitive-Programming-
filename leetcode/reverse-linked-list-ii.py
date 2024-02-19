# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head is None or head.next is None:
            return head
        
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
    
        for _ in range(left - 1):
            prev = prev.next
        
    
        current = prev.next
        next_node = current.next
        
    
        for _ in range(right - left):
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = current.next
        
        return dummy.next