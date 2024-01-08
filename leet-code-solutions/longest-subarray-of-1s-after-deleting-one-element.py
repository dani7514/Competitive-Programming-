class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        set1 = []
        set2 = []
        element_deleted = False
        maxelement = 0
        for i in range(len(nums)):
            value = nums[i]
            if value == 1 and not element_deleted:
                set1.append(value)
            elif value == 1 and element_deleted:
                set2.append(value)
            elif value == 0 and element_deleted:
                maxelement = max(maxelement,len(set1)+len(set2))
                set1,set2 = set2,[]
            elif value ==0 and not element_deleted:
                element_deleted = True
        return max(maxelement,len(set1)+len(set2)) if element_deleted else max(maxelement,len(set1)+len(set2)) - 1
