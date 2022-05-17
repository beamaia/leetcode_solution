class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
                
        index = 0
        longest_string = s[0]
        long_len = 1
        total_len = len(s)
        
        while total_len >= index:
            letter_set = set(s[index])
            aux_string = s[index]
            
            next_letter_index = index + 1
            while next_letter_index < total_len and s[next_letter_index] not in letter_set:
                letter_set.add(s[next_letter_index])
                aux_string += s[next_letter_index]
                next_letter_index += 1
                
            aux_len = len(aux_string)
            
            if aux_len > long_len:
                longest_string = aux_string
                long_len = aux_len
                
            if long_len + index >= total_len:
                break
            
            index += 1
        
        return long_len


val = "dcdf"
print(Solution().lengthOfLongestSubstring(val))