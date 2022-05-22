# runtime, brute force
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_val = 2**31 - 1        
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1

        if sign == 1 and dividend >= max_val:
            return max_val
        elif sign == -1 and dividend <= -(max_val+1):
            return -(max_val + 1)
        
        dividend = abs(int(dividend))
        divisor = abs(divisor)
            
        counter = 0        
        while dividend > 0:
            dividend -= divisor
            
            if max_val <= counter:
                break
                
            if dividend >= 0:
                counter += 1
            else:
                break
        
        if sign == 1 and counter > max_val:
            return max_val
        elif sign == -1 and counter > max_val + 1:
            return (max_val + 1) * -1
        
        return  counter * sign

a = -2147483648
b = -1

print(Solution().divide(a, b))