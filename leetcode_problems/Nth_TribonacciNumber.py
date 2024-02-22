class tribonacciNumber:

    def tribonacci(self, n):
        s1, s2, s3 = 0, 1, 1
        if n == 0:
            return s1
        if n == 1:
            return s2
        if n == 2:
            return s3
        a = 3
        while a <= n:
            ans = s1 + s2 + s3
            s1, s2, s3 = s2, s3, ans
            a += 1
        return ans


t = tribonacciNumber()
n = 4
print(t.tribonacci(n))
