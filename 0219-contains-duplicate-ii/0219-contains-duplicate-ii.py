class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i-dic[nums[i]]<=k:
                    return True
                else:
                    dic[nums[i]]+=i
            else:
                dic[nums[i]]=i
        else:
            return False

            
        