class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c = {}
        c[')'] = '('
        c['}'] = '{'
        c[']'] = '['
        
        for x in s:
            if x in c:
                if stack and stack[-1] == c[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False

        