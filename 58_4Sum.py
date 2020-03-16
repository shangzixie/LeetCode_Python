class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        self.results = []
        self.dfs([], numbers, target, 0)
        return self.results

    def dfs(self, path, numbers, target, startIndex):
        if target < 0:
            return
        if len(path) == 4 and target == 0:
            self.results.append(list(path))
            return
        if len(path) == 4:
            return

        for i in range(startIndex, len(numbers)):
            target -= numbers[i]
            self.dfs(path + [numbers[i]], numbers, target, i)
            target += numbers[i]


if __name__ == '__main__':
    solution = Solution()
    numbers =[2,7,11,15]
    target = 3
    solution.fourSum(numbers, target)