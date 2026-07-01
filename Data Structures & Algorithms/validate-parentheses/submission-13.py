class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {"]":"[", ")":"(", "}":"{"}

        for b in s:
            if stack:
                if b in valid:
                    if stack[-1] != valid[b]:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)
        return not stack