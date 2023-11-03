class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=[]
        i,j=0,len(numbers)-1
        
        while i<j:
            print(i,j)
            if numbers[i]+numbers[j]==target:
                arr.append(i+1)
                arr.append(j+1)
                i+=1
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
        return arr
            