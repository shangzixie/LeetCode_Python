class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):

        self.visited = {}
        return self.dfs(grid, 0, 0)

    def dfs(self, grid, x, y):
        if (x, y) in self.visited:
            return self.visited[(x, y)]
        if x == len(grid) or y == len(grid[0]):
            return float("inf")
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return grid[x][y]

        down = self.dfs(grid, x + 1, y)
        right = self.dfs(grid, x, y + 1)

        pathSum = min(down, right) + grid[x][y]
        self.visited[(x, y)] = pathSum

        return pathSum


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    solution.minPathSum(grid)