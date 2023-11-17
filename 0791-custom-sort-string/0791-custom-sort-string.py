class Solution:
    def customSortString(self, order: str, s: str) -> str:
        both={}
        dif=''
        for i in s:
            if i in order:
                if i in both:
                    both[i]+=1
                else:
                    both[i]=1       
            else:
                dif+=i
     
        custom=''
        for j in order:
            if j in both:
                custom+=(both[j] *j)
         
        custom+=dif
        return custom
        
        