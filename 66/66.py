class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        index = len(digits) - 1

        while carry and index > -1:
            digits[index] += 1
        
            if digits[index] > 9:
                carry = 1
                digits[index] -= 10
            else:    
                carry = 0
                break
            
            index -= 1
            
        
        if carry:
            digits.insert(0, 1)
            

        return digits
                       
if __name__ == '__main__':
    sol = Solution()
    print(*sol.plusOne([9, 9]))