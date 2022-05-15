class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)

        if b == '0':
            return a
        if a == '0':
            return b
        if a == b == '0':
            return a
        
        if len_a > len_b:
            max_ = len_a
        else:
            max_ = len_b
        
        iter_ = 0
        sol = ['0'] * (max_ + 1)
        carry = 0
        
        while max_ - iter_:
            aux = 0 + carry
            
            if len_a > iter_:
                aux += int(a[len_a - iter_ - 1])
            
            if len_b > iter_:
                aux += int(b[len_b - iter_ - 1])
                
            if aux % 2:
                sol[max_ - iter_ ] = '1'
                
                if aux == 3:
                    carry = 1
                else:
                    carry = 0
            else:
                sol[max_ - iter_ ] = '0'
                
                if aux == 2:
                    carry = 1
                else:
                    carry = 0
            iter_ += 1
        
        if carry:
            sol[0] = '1'
            return ''.join(sol)    
        if sol[0] == '0':
            return ''.join(sol[1:])
        return ''.join(sol)

                
if __name__ == '__main__':
    sol = Solution()
    a = "100"
    b = "110010"

    print(sol.addBinary(a=a, b=b))
