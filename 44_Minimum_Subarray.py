class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):

        prefixSum = 0
        maxsum = 0
        res = float("inf")

        for i in range(len(nums)):
            prefixSum += nums[i]
            maxsum = max(maxsum, prefixSum)
            res = min(prefixSum - maxsum, res)

        return res