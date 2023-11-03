class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        k=set()
        p=set()
        
        for i in nums2:
            k.add(i)
        
        for j in nums1:
            if j in k:
                p.add(j)
                
        if not p:  
            return -1
        
        small=min(p)
        return small
        