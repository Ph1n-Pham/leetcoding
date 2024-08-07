'''
https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        n = len(digits)
        for i in range(n-1, -1, -1):
            if i == n - 1:
                new = digits[i] + carry + 1
            else:    
                new = digits[i] + carry
            # print(new)
            carry = new // 10
            new_digit = new % 10

            digits[i] = new_digit
            # print(digits[i])
        
        if carry == 1:
            digits.insert(0, 1)

        return digits
