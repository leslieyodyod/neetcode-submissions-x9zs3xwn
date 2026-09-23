class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for d in details:
            d = list(d)
            age = int("".join(d[-4:-2]))
            if age > 60:
                res += 1
        return res
