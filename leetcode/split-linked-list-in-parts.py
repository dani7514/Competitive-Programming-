# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
    
        while temp:
            temp = temp.next
            n += 1

        
        l_list = n // k
        extra = n % k
        res = []
        i = 0

        while i < k:
            part_size = l_list + 1 if extra > 0 else l_list
            extra -= 1

        
            part_head = head
            part_prev = None
            for _ in range(part_size):
                if head:
                    part_prev = head
                    head = head.next

            if part_prev:
                part_prev.next = None 

            res.append(part_head)
            i += 1

        return res