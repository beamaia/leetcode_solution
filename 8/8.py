class Solution:
    def myAtoi(self, s: str) -> int:
        if not len(s):
            return 0
        
        while True:
            if not len(s):
                return 0 
        
            if s[0] == " ":
                s = s[1:]
            else:
                break
                
        integer = 0
        sign = 1
        lim_min = (-2)**31
        lim_max = (2**31 -1)
        
        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s =s[1:]
        elif not ("0" <= s[0] <= "9"):
            return integer
        
        for i in range(len(s)):
            if not ("0" <= s[i] <= "9"):
                break

            aux = int(s[i])
            integer = integer*10 + aux
        
        integer = integer * sign
        
        if lim_min <= integer <= lim_max:
            return integer
        elif lim_min > integer:
            return lim_min
        else:
            return lim_max

value = "3.14"
print(Solution().myAtoi(value))