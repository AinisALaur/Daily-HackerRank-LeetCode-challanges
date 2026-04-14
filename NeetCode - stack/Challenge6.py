class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        arr =[]

        for i in range(len(tokens)):
            symbol = tokens[i]
            if symbol != '+' and symbol != '*' and symbol != '-' and symbol != '/':
                arr.append(int(symbol))

            else:
                operator = symbol
                if operator == '+':
                    operand1 = arr.pop()
                    operand2 = arr.pop()
                    arr.append(operand2 + operand1)

                if operator == '-':
                    operand1 = arr.pop()
                    operand2 = arr.pop()
                    arr.append(operand2 - operand1)

                if operator == '*':
                    operand1 = arr.pop()
                    operand2 = arr.pop()
                    arr.append(operand2 * operand1)


                if operator == '/':
                    operand1 = arr.pop()
                    operand2 = arr.pop()
                    arr.append(int(operand2 / operand1))   

        return arr.pop()
        

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))