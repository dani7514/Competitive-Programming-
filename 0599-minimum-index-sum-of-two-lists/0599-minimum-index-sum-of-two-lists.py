class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = {}
        minimum_index = float('inf')

        for string in range(len(list1)):
            if list1[string] in list2:
                temp_index_list2 = list2.index(list1[string])
                minimum[list1[string]] = temp_index_list2 + string
                if  temp_index_list2 + string < minimum_index:
                    minimum_index = temp_index_list2 + string
        result = []
        for j in minimum:
            if minimum[j] == minimum_index:
                result.append(j)
                
        return result
       
                
        