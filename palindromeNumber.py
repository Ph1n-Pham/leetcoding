'''
https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases
        if x == 0:
            return True
        elif x < 0:
            return False
        elif x < 10:
            return True
        
        str_x = str(x)
        n = len(str_x)
        
        for i in range(0, n//2):
            if str_x[i] != str_x[-i-1]:
                return False
        return True
