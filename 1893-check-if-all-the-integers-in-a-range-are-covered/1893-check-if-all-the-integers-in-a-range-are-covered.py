class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ranges.sort(key=lambda x: x[0])
        print(ranges)
        max_end = left - 1

        for start, end in ranges:
            if start > max_end + 1:
                return False
            max_end = max(max_end, end)

            if max_end >= right:
                return True

        return False

            
            
        
        