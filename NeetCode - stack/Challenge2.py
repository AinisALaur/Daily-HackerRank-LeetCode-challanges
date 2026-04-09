class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if(p == '(' or p == '[' or p =='{'):
                stack.append(p)
            
            elif(p == ')' or p == ']' or p =='}'):
                if(len(stack) <= 0):
                    return False

                elif(p == ')' and stack[-1] != '('):
                    return False

                elif(p == '}' and stack[-1] != '{'):
                    return False

                elif(p == ']' and stack[-1] != '['):
                    return False

                else:
                    stack.pop()

        return len(stack) == 0
    
sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("(]"))
print(sol.isValid("(((((((())))))))"))
print(sol.isValid("({}{})"))