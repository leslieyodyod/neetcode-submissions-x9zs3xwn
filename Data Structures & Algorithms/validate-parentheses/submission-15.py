class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if stack:
                if char in brackets:
                    if stack[-1] == brackets[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
                
            else:
                stack.append(char)
        return len(stack) == 0