"""
Write a Python library for parsing and evaluating mathematical expressions.
"""
import operator

class ExpressionEvaluator:
    def __init__(self):
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def evaluate(self, expr):
        tokens = self.tokenize(expr)
        postfix = self.infix_to_postfix(tokens)
        return self.eval_postfix(postfix)

    def tokenize(self, expr):
        return expr.replace('(', ' ( ').replace(')', ' ) ').split()

    def infix_to_postfix(self, tokens):
        precedence = {'+':1, '-':1, '*':2, '/':2}
        output = []
        stack = []

        for token in tokens:
            if token.isdigit():
                output.append(int(token))
            elif token in self.ops:
                while (stack and stack[-1] in self.ops and
                       precedence[stack[-1]] >= precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())

        return output

    def eval_postfix(self, postfix):
        stack = []

        for token in postfix:
            if isinstance(token, int):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                result = self.ops[token](a, b)
                stack.append(result)

        return stack[0]


calc = ExpressionEvaluator()

expr = "3 + 5 * ( 2 - 1 )"
print("Result:", calc.evaluate(expr))