class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return helper(x*x, n//2)
            else:
                return helper(x*x, (n-1)//2)*x

        if n < 0:
            n = -n
            x = 1/x

        return helper(x, n)


class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        ans = 1
        while n > 0:
            if n % 2 == 0:
                x *= x
                n = n // 2
            ans *= x
            n -= 1
        return ans


s = Solution1
print(s.myPow(s, x=2.0, n=10))
