class Solution1:
    def longestIncreasingPath(self, matrix):
        self.DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        output = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = self.dfs(matrix, i, j, memo)
                output = max(output, length)

        return output

    def dfs(self, matrix, i, j, memo):
        if memo[i][j] != 0:
            return memo[i][j]
        # if up down left right <= matrix[i][j]:
        #     return 0

        maxLength = 1
        for dx, dy in self.DIRECTION:
            x = dx + i
            y = dy + j
            if x >= len(matrix) or x < 0 or y >= len(matrix[0]) or y < 0:
                continue
            length = self.dfs(matrix, x, y, memo)
            maxLength = max(length, maxLength)

        memo[i][j] = maxLength
        return memo[i][j]
    """
    版本一：  没有加递增的比较
    """
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        版本二：
            增加比较
        """
        self.DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        output = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = self.dfs(matrix, i, j, memo)
                output = max(output, length)

        return output

    def dfs(self, matrix, i, j, memo):
        if memo[i][j] != 0:
            return memo[i][j]
        # if up down left right <= matrix[i][j]:
        #     return 0

        maxLength = 1
        for dx, dy in self.DIRECTION:
            x = dx + i
            y = dy + j
            if x >= len(matrix) or x < 0 or y >= len(matrix[0]) or y < 0 or matrix[x][y]<= matrix[i][j]:
                continue
            length = self.dfs(matrix, x, y, memo) +1 
            maxLength = max(length, maxLength)

        memo[i][j] = maxLength
        return memo[i][j]
    """
    版本一：  没有加递增的比较
    """

if __name__ == '__main__':
    a = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    a.longestIncreasingPath(matrix)