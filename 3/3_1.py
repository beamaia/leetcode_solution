class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        
        longest_string = s[0]
        letter_set = set(s[0])
        long_len = 1
        aux_string = s[0]
        
        for letter in list(s[1:]):
            print(aux_string)
            if letter in letter_set:
                letter_set = set(letter)
                
                aux_search_string = letter
                for i in range(len(aux_string) - 1, -1, -1):
                    aux_letter = aux_string[i]
                    if aux_letter != letter:
                        aux_search_string = aux_letter + aux_search_string
                        letter_set.add(aux_letter)
                    else:
                        break
                aux_string = aux_search_string
            else:
                aux_string += letter
                letter_set.add(letter)
                
                if len(aux_string) > long_len:
                    longest_string = aux_string
                    long_len = len(aux_string)
        
        return len(longest_string)

val = "abcabcbb"
print(Solution().lengthOfLongestSubstring(val))