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
                self.stack.pop()  # 여는 괄호 제거

            else:
                while (
                    self.stack
                    and self.precedence(self.stack[-1]) >= self.precedence(token)
                ):
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
        # 117.32처럼 여러 글자로 된 수도 한 토큰으로 읽는다.
        return re.findall(r'\d+(?:\.\d+)?|[()+*/^-]', expression)

    def is_operand(self, token):
        return token[0].isdigit()


# 추가 테스트 
postfix = Infix2Postfix()
print(postfix.infix_to_postfix("1-3*2"))
print(postfix.infix_to_postfix("(117.32+83)*49"))