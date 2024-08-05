'''
https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:    # If carry = 1 then loop continues
            digit_a = int(a[i]) if i >= 0 else 0    # Else 0 to avoid out of index
            digit_b = int(b[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry
            carry = total // 2
            result.append(str(total % 2))
            i -= 1
            j -= 1

        # Reverse the result and join to form the final binary string
        return ''.join(result[::-1])
