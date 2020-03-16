class Solution:
    def find(self, M, N, matrix):

        # [0][j]
        for i in [0, M - 1]:
            for j in range(N):
                if matrix[i][j] == "*":
                    continue
                self.dfs(matrix, i, j)
        print(1)
        for j in [0, N - 1]:
            for i in range(M):
                if matrix[i][j] == "*":
                    continue
                self.dfs(matrix, i, j)

        res = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == ".":
                    res += 1

        return res

    def dfs(self, matrix, i, j):
        if matrix[i][j] == "*":
            return

        matrix[i][j]  = "*"
        for deti, detj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nexti = deti + i
            nextj = detj + j
            if nexti < 0 or nexti >= len(matrix):
                continue
            if nextj < 0 or nextj >= len(matrix[0]):
                continue
            if matrix[nexti][nextj] == "*":
                continue
            self.dfs(matrix, nexti, nextj)




if __name__ == '__main__':
    matrix = [[".", "*", "*", "."], ["*", ".", "*", "."], ["*", ".", ".", "*"], ["*", "*", "*", "*"]]
    solution = Solution()
    M = len(matrix)
    N = len(matrix[0])
    result = solution.find(M, N, matrix)
    print(result)
