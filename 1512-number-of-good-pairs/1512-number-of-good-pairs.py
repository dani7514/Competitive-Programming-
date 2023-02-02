class Solution(object):
    def numIdenticalPairs(self, nums):
        output = 0
        dict_number = {}
        for n in nums:
            if n in dict_number:
                output += dict_number[n]
                dict_number[n] += 1
            else:
                dict_number[n] = 1
            print(dict_number)
        return output
        
        
        
        