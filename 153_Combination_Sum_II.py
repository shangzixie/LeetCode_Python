class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, nums, target):
        nums.sort()
        self.result = []
        self.dfs(nums, target, 0, [])

        return self.result

    def dfs(self, nums, target, startIndex, path):
        if target < 0:
            return
        if target == 0:
            self.result.append(list(path))
            return

        for i in range(startIndex, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i > startIndex:
                continue
            path.append(nums[i])
            self.dfs(nums, target - nums[i], i + 1, path)
            path.pop()


if __name__ == '__main__':
    solution = Solution()
    nums= [1,1,6,7]
    target = 8
    solution.combinationSum2(nums, target)

