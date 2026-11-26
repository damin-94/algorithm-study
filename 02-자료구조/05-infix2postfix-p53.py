# 2장 53쪽 - 중위 표기식을 후위 표기식으로 변환
# 거듭제곱(^)은 오른쪽부터 묶이도록 처리한다.

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
                # 53쪽 수정 부분
                while self.stack:
                    top = self.stack[-1]

                    if self.precedence(top) < self.precedence(token):
                        break

                    # 우선순위가 같고 새 연산자가 ^이면 기존 ^를 스택에 둔다.
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


# 테스트 - 53쪽 PPT의 두 식
postfix = Infix2Postfix()
print(postfix.infix_to_postfix("2*3*4"))
print(postfix.infix_to_postfix("2^3^2"))