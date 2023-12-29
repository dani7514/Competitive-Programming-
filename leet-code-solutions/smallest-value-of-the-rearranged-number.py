class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        is_negative = num < 0
        num = abs(num)
        arr = []

        for i in str(num):
            arr.append(int(i))

        arr.sort()
        if not is_negative:
            for i in range(len(arr)):
                if arr[i] != 0:
                    arr[0], arr[i] = arr[i], arr[0]
                    break
        else:
            arr = arr[::-1]
        
        result = "".join(map(str,arr))

        if is_negative:
            return int("-" + result)
        else:
            return int(result)


        
        