from collections import deque
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        q = deque()
        #[left or right shift, amount to be shifted]
        #left shift = remove first char and append to end
        #right shift = remove last char and add to beginning
        s = list(s)

        for i in shift:
            if i[0] == 0:
                for i in range(i[1]):
                    char = s[0]
                    s = s[1:]
                    s.append(char)
            elif i[0] == 1:

                for i in range(i[1]):
                    char = [s[-1]]
                    s = s[:-1]
                    newStr = char + s
                    s = newStr
        return "".join(s)



        
        


        


