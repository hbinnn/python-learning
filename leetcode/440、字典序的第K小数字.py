class Solution:
    def getCount(self, prefix, n):
        cur = prefix
        nex = prefix + 1
        count = 0
        while cur <= n:
            count += min(n+1, nex) - cur
            cur *= 10
            nex *= 10
        return count

    def findKthNumber(self, n: int, k: int) -> int:
        p = 1
        prefix = 1
        while p < k:
            count = self.getCount(prefix, n)

            if p + count > k:
                prefix *= 10
                p += 1
            else:
                prefix += 1
                p += count

        return prefix



