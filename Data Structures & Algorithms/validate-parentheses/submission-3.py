class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening == '(' and b != ')':
                    return False
                elif opening == '[' and b != ']':
                    return False
                elif opening == '{' and b != '}':
                    return False
        
        return True if not stack else False