class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                open = stack[-1]

                if open == '(' and char != ')' or open == '[' and char != ']' or open == '{' and char != '}':
                    return False
                
                stack.pop()
            
        if len(stack) == 0:
            return True
        
        return False

                    