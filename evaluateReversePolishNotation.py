'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ariths = ['+', '-', '*', '/']
        # define operators
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)}   # The division between two integers always truncates toward zero.

        stack = []
        for i in tokens:
            # add in stack if not an arithmetics
            if i not in ariths:
                stack.append(int(i))
            # if an arith then pop last two numbers in stack, perform arith, then add the result
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                val = op[i](num1, num2)
                stack.append(val)
        return stack[0] # result should be the last element in the stack
