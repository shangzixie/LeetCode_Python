class Solution1:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        self.results = []
        self.dfs(n, [], 2)

        return self.results

    def dfs(self, n, path, startIndex):
        if n == 1 and len(path) != 1:
            self.results.append(list(path))
            return

        for i in range(startIndex, n + 1):
            if n % i != 0:
                continue
            if i > (n / i):
                break
            path.append(i)
            self.dfs(int(n / i), path, i)
            path.pop()

        if n >= startIndex:
            path.append(n)
            self.dfs(1, path, n)
            path.pop()
        """
        减枝不彻底
        """


class Solution2:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        self.results = []
        self.dfs(n, [], 2)

        return self.results

    def dfs(self, n, path, startIndex):
        if n == 1 and len(path) != 1:
            self.results.append(list(path))
            return

        import math
        for i in range(startIndex, int(math.sqrt(n) + 1)):
            if n % i != 0:
                continue
            path.append(i)
            self.dfs(int(n / i), path, i)
            path.pop()

        if n >= startIndex:
            path.append(n)
            self.dfs(1, path, n)
            path.pop()


class Solution:
    """
    @param n: An integer
    @return: a list of combination
    最终版
    """

    def getFactors(self, n):
        self.results = []
        self.dfs(n, [], 2)

        return self.results

    def dfs(self, n, path, startIndex):
        if len(path) != 0:
            self.results.append(path[:] + [n])

        import math
        for i in range(startIndex, int(math.sqrt(n) + 1)):
            if n % i != 0:
                continue
            path.append(i)
            self.dfs(int(n / i), path, i)
            path.pop()


if __name__ == '__main__':
    solution = Solution2()
    solution.getFactors(32)

