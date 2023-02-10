# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp =  head
        length = 0
        while temp:                 
            length +=1
            temp = temp.next
        if length-n==0:
            head = head.next
            return head
        
        new = head
        for i in range(length-n):
            prev = new
            new = new.next
        prev.next = new.next
        new.next = None
        return head   
        