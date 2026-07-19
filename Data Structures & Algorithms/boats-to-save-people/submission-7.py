class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res, boat = [], []

        people.sort()

        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                res.append([people[l], people[r]])
                l += 1
            else:
                res.append([people[r]])
            r -= 1
        return len(res)


        