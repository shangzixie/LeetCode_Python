class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b

        res = 1
        while n > 1:
            if n % 2 != 0:
                res = a
                n = n - 1

            a *= a
            n /= 2

        return a * res % b


if __name__ == '__main__':
    solution = Solution()
    solution.fastPower(11,123898 ,12345)