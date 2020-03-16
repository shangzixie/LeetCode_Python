class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x

        init = 1
        while n > 1:
            if n % 2 == 1:
                init *= x

            x = x * x
            n = n / 2

        return x * init


if __name__ == '__main__':
    solution = Solution()
    x= 9.88
    n = 3
    solution.myPow(x,n)