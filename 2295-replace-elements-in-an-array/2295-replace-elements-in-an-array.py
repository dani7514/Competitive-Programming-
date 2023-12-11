class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictionary = {}
        for k in range(len(nums)):
            dictionary[nums[k]] = k
        for i in range(len(operations)):
            index = dictionary[operations[i][0]]
            l = dictionary[operations[i][0]]
            del dictionary[operations[i][0]]
            dictionary[operations[i][1]] = l
            nums[index] = operations[i][1]
        return nums