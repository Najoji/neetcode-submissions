class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for c in tokens:
            if c == "+":
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif c == "-":
                rhs = self.stack.pop()
                lhs = self.stack.pop()
                self.stack.append(lhs - rhs)
            elif c == "/":
                rhs = self.stack.pop()
                lhs = self.stack.pop()
                self.stack.append(int(lhs / rhs))
            elif c == "*":
                self.stack.append(self.stack.pop() * self.stack.pop())
            else :
                self.stack.append(int(c))
        return self.stack[0]


        