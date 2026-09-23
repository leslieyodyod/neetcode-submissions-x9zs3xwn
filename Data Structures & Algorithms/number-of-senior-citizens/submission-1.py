class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        details = [list(d) for d in details]
        for d in details:
            age = int("".join(d[-4:-2]))
            if age > 60:
                res += 1
        return res
