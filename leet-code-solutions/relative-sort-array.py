class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        contain_in_arr2={}
        not_in_arr2=[]
        
        for i in arr1:
            if i in arr2:
                if i not in contain_in_arr2 :
                    contain_in_arr2[i]=1
                else:
                    contain_in_arr2[i]+=1
            else:
                not_in_arr2.append(i)
        print(contain_in_arr2)
        new_arr=[]
        for j in arr2:
            for _ in range(contain_in_arr2[j]):
                new_arr.append(j)

        not_in_arr2.sort()

        return new_arr + not_in_arr2
        