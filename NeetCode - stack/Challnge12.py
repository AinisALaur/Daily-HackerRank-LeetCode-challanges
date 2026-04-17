class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == ']':
                subStr = ""
                while stack[-1] != '[':
                    subStr = stack.pop() + subStr
                stack.pop()

                n = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    n = stack.pop() + n

                for i in range(int(n)):
                    for char in subStr:
                        stack.append(char)
                
            else:
                stack.append(s[i])

        return "".join(stack)
    
sol = Solution()
print(sol.decodeString("3[a2[bc]]"))