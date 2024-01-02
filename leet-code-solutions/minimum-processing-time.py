class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse= True)
        tasks.sort()
        j = 0
        result = []
        for i in range(1,len(tasks)+1):
            if i % 4 == 0:
                result.append(processorTime[j] + tasks[i-1])
                j += 1
            else:
                result.append(processorTime[j] + tasks[i-1])

        return max(result)

            