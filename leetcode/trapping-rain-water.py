class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)

        left = 0
        for i in range(len(height)):
            if height[i] > left:
                left_max[i] = height[i]
                left = height[i]
            else:
                left_max[i] = left

        right = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] > right:
                right_max[i] = height[i]
                right = height[i]
            else:
                right_max[i] = right

        result = []
        for i in range(len(height)):
            temp = min(left_max[i] , right_max[i])
            dif = temp - height[i]
            result.append(dif)

        return sum(result)
