class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):

        return self.dfs(nums, 0, float("-inf"), dict())

    def dfs(self, nums, curindex, lastNum, memo):
        if curindex >= len(nums):
            return 0
        if curindex in memo:
            return memo[curindex]

        # take
        taken = 0
        if nums[curindex] > lastNum:
            taken = self.dfs(nums, curindex + 1, nums[curindex], memo) + 1

            # untaken
        untaken = self.dfs(nums, curindex + 1, nums[curindex], memo)

        memo[curindex] = max(taken, untaken)

        print(memo)
        return memo[curindex]


if __name__ == '__main__':
    solution = Solution()
    nums= [-2,-1,2,5,6,7]
    solution.longestIncreasingSubsequence(nums)