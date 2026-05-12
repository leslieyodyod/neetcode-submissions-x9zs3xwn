class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0

        seen = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                idx = local.index('+')
                local = local[:idx]
            joined = str(local + domain)
            seen.add(joined)


        return len(seen)