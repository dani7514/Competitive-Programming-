class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        container={}
        for i in range(len(names)):
            container[heights[i]]=names[i]

        # Selection sort

        # for i in range(len(heights)):
        #     min_index = i

        #     for j in range(i+1,len(heights)):
        #         if heights[j] < heights[min_index]:
        #             min_index = j

        #     heights[i], heights[min_index] = heights[min_index] , heights[i]

        # prone Bubble sort

        flag = True
        for i in range(len(heights)):
            for j in range(len(heights)-1):
                if heights[j] > heights[j+1]:
                    flag = False
                    heights[j], heights[j+1] = heights[j+1], heights[j]
            if flag:
                break

        # insertion sort
    
        # for i in range(1,len(heights)):
        #     key = heights[i]
        #     j = i - 1

        #     while j >= 0 and heights[j] >= key:
        #         heights[j+1] = heights[j]
        #         j -= 1

        #     heights[j+1] = key

        arr=[]
        for i in range(len(heights)-1,-1,-1):
            temp = heights[i]
            arr.append(container[temp])
        
        return arr
