# 2장 54쪽 - 중위 표기식을 후위 표기식으로 바꾸고 계산하기
import re


class Infix2Postfix:
    def infix_to_postfix(self, expression):
        self.stack = []
        self.output = []

        expression = self.tokenization(expression)

        for token in expression:
            if self.is_operand(token):
                self.output.append(token)

            elif token == '(':
                self.stack.append(token)

            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()

            else:
                while self.stack:
                    top = self.stack[-1]

                    if self.precedence(top) < self.precedence(token):
                        break

                    if self.precedence(top) == self.precedence(token) and token == '^':
                        break

                    self.output.append(self.stack.pop())

                self.stack.append(token)

        while self.stack:
            self.output.append(self.stack.pop())

        return ' '.join(self.output)

    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0

    def tokenization(self, expression):
        return re.findall(r'\d+(?:\.\d+)?|[()+*/^-]', expression)

    def is_operand(self, token):
        return token[0].isdigit()


# 54쪽 - 후위 표기식 계산
def evaluate_postfix(postfix):
    stack = []

    for token in postfix.split():
        if token not in ('+', '-', '*', '/', '^'):
            stack.append(float(token))
            continue

        op2 = stack.pop()
        op1 = stack.pop()

        if token == '+':
            stack.append(op1 + op2)
        elif token == '-':
            stack.append(op1 - op2)
        elif token == '*':
            stack.append(op1 * op2)
        elif token == '/':
            stack.append(op1 / op2)
        elif token == '^':
            stack.append(op1 ** op2)

    return stack.pop()


# 54쪽 PPT 예제
if __name__ == "__main__":
    expression = "3.5+5*(2^3-40.11)^(2+1*2.0)-8.5"

    converter = Infix2Postfix()
    postfix = converter.infix_to_postfix(expression)

    print(postfix)  
    print(evaluate_postfix(postfix))