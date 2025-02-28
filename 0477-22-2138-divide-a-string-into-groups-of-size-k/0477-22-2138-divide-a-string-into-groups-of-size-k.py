class Solution:
    def divideString(self, s, k, fill):
        len_s = len(s)

        ret_val = []

        start_index = 0
        end_pos = start_index + k
        while (end_pos <= len_s):
            ret_val.append(s[start_index:end_pos])
            
            start_index += k
            end_pos += k
        
        if (end_pos - len_s < k):
            ret_val.append(s[start_index:end_pos] + (end_pos-len_s) * fill)
        
        return ret_val