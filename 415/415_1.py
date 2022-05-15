# without using int, str and join
class Solution:

    def listStr(self, values:list) -> str:
        aux = ''
        for i in values:
            aux += i
        
        return aux

    def addStrings(self, num1: str, num2: str) -> str:
        num1_str = [digit for digit in num1]
        num2_str = [digit for digit in num2]

        if len(num1_str) > len(num2_str):
            biggest_len = len(num1_str)
            smallest_len = len(num2_str)
            num2_str = ['0']*(biggest_len - smallest_len) + num2_str
        elif len(num2_str) > len(num1_str):
            biggest_len = len(num2_str)
            smallest_len = len(num1_str)
            num1_str = ['0']*(biggest_len - smallest_len) + num1_str
        else:
            biggest_len = len(num1_str)
        

        total_sum = ['0']*(biggest_len + 1)
              
        for i in range(biggest_len - 1, -1, -1):
            aux_sum = ord(num1_str[i]) +  ord(num2_str[i]) + ord(total_sum[i + 1]) - 3*ord('0')
            carry_val = 0
            
            if aux_sum > 9: 
                carry_val = 1
                aux_sum -= 10
            
            chr_total_sum = chr(aux_sum + ord('0'))
            chr_carry = chr(carry_val + ord('0'))

            total_sum[i + 1] = chr_total_sum            
            total_sum[i] = chr_carry
        
        if not carry_val:
            total_sum = total_sum[1:]

        return self.listStr(total_sum)
    
                

sol = Solution()
print(sol.addStrings('9133', '0'))           

            
            