class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        operations = list(operations)

        for op in operations:
            if stack:
                if op == "+":
                    stack.append(stack[-1]+stack[-2])
                elif op == "D":
                    stack.append(stack[-1] * 2)
                elif op == "C":
                    stack.pop()
                else:
                    stack.append(int(op))
            else:
                stack.append(int(op))
        return sum(stack) 