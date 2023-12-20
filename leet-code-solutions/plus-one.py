class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        convert_to_string = ''.join(str(num) for num in digits)
        add_one = str(int(convert_to_string) + 1)
        result =[]

        for i in add_one:
            result.append(int(i))

        return result