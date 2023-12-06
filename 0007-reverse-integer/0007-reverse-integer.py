class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        
        if abs(x) != x:
            is_negative = True
        
        to_string = str(x)
        reverse_it = to_string[::-1]
        
        if is_negative:
            temporary_string = "-" + reverse_it[:len(reverse_it)-1]
            if (-2)**31 < int(temporary_string) < (2)**31 -1:
                return int(temporary_string)
            else:
                return 0
        else:
            if (-2)**31 < int(reverse_it) < (2)**31 -1:
                return int(reverse_it)
            else:
                return 0
        
        
            