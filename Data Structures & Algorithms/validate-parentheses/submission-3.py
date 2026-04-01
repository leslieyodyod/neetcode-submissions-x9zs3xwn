class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if stack and char in valid:
                if stack.pop() != valid[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        