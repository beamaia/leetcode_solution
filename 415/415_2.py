# using int, str, join
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not len(num1) or num1 == '0':
            return num2
        if not len(num2) or num2 == '0':
            return num1

        if len(num1) > len(num2):
            biggest_len = len(num1)
            smallest_len = len(num2)
            num2 = '0'*(biggest_len - smallest_len) + num2
        elif len(num2) > len(num1):
            biggest_len = len(num2)
            smallest_len = len(num1)
            num1 = '0'* (biggest_len - smallest_len) + num1
        else:
            biggest_len = len(num1)
        

        total_sum = ['0']*(biggest_len + 1)
              
        for i in range(biggest_len - 1, -1, -1):
            aux_sum = int(num1[i]) +  int(num2[i]) + int(total_sum[i + 1])
            carry_val = 0
            
            if aux_sum > 9: 
                carry_val = 1
                aux_sum -= 10
            
            total_sum[i + 1] = str(aux_sum)            
            total_sum[i] = str(carry_val)
        
        if not carry_val:
            total_sum = total_sum[1:]

        return ''.join(total_sum)