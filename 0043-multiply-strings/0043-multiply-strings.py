class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            carry = 0
            for j in range(len2 - 1, -1, -1):
                temp_sum = int(num1[i]) * int(num2[j]) + result[i + j + 1] + carry
                result[i + j + 1] = temp_sum % 10
                carry = temp_sum // 10

            result[i + j] += carry

        result_str = ''.join(map(str, result)).lstrip('0')
        
        if result_str:
             return result_str
        else:
            return '0'

            
            
                
            
        
        