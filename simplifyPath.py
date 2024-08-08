'''
https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

Generate stack, and append()/pop() for each cases
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by '/'
        components = path.split('/')
        
        for component in components:
            if component == '' or component == '.':
                # Skip empty components or current directory indicators
                continue
            elif component == '..':
                # Pop from stack if not empty
                if stack:
                    stack.pop()
            else:
                # Push valid directory names to the stack
                stack.append(component)
        
        # Join the stack to form the simplified canonical path
        simplified_path = '/' + '/'.join(stack)
        return simplified_path
