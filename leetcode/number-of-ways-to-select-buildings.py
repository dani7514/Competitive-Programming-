class Solution:
    def numberOfWays(self, s: str) -> int:
        temp_dict = defaultdict(int)

        for i in s:
            if i == '0':
                temp_dict['0'] += 1
                temp_dict['10'] +=  temp_dict['1']
                temp_dict['010'] +=  temp_dict['01']
                
            else:
                temp_dict['1'] += 1
                temp_dict['01'] += temp_dict['0']
                temp_dict['101'] += temp_dict['10']
                

        return  temp_dict['101'] +  temp_dict['010']