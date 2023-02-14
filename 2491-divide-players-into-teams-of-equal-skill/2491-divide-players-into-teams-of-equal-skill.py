class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        arr=[]
        right=len(skill)-1
        chemistry=0
        for i in range(len(skill)):
            if i<right:
                arr.append(skill[i]+skill[right])
               
                if arr[i]==arr[0]:
                    chemistry+=(skill[i]*skill[right])
                else:
                    return -1
            right-=1
            
        return chemistry

            
            
            
        
        