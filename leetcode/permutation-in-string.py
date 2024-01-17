class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_dict = {}

        for i in s1:
            freq_dict[i] = freq_dict.get(i, 0) + 1

        for i in range(len(s2)- len(s1) + 1):
            temp_dict = {}
            j = i
            while j < (len(s1) + i):
                temp_dict[s2[j]] = temp_dict.get(s2[j], 0) + 1
                j += 1

            if temp_dict == freq_dict:
                return True

        return False
            


