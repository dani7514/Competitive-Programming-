class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        container={}
        for i in range(len(names)):
            container[heights[i]]=names[i]
        
        sorted_heights=sorted(heights)
        arr=[]
        for i in range(len(sorted_heights)-1,-1,-1):
            temp=sorted_heights[i]
            arr.append(container[temp])
        
        return arr
