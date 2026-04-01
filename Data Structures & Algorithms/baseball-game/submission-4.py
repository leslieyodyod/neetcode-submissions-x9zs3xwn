class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if stack:
                if op == "+":
                    stack.append(sum(int(i) for i in stack[-2:]))
                    print(stack)
                elif op == "D":
                    stack.append(int(stack[-1]) * 2)
                    print(stack)
                elif op == "C":
                    stack.pop()
                    print(stack)
                else:
                    stack.append(int(op))
                    print(stack)
            else:
                stack.append(int(op))
                print(stack)
        return sum(int(i) for i in stack)