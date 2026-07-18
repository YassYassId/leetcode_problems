class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                second_operand = stack.pop()
                result = self.apply_op(tokens[i], stack.pop(), second_operand)
                stack.append(result)
        return stack[-1]

    def apply_op(self, op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return int(a / b)
        