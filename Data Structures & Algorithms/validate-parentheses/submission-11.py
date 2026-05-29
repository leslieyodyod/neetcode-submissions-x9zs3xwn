class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"}":"{", "]":"[", ")":"("}
         
        for char in s:
            if stack:
                if char in parentheses and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return len(stack) == 0

        


        
        

        