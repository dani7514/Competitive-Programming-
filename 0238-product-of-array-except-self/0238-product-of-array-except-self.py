class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        prod1=math.prod(nums)
        count=nums.count(0)
        if count==1:
                prod2=math.prod([i for i in nums if i!=0 ])
        for i in nums:
                if i==0 and count>1:
                        l.append(0)
                elif i==0 and count==1:
                        l.append(prod2)
                else:
                        l.append(prod1//i)
        return l
        