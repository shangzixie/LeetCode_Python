class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        pre2index = {0: 0}
        prefixSum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            if prefixSum in pre2index:
                return [pre2index[prefixSum], i ]
            else:
                pre2index[prefixSum] = i+1




if __name__ == '__main__':
    a = Solution()
    nums = [-3,1,2,-3,4]
    a.subarraySum(nums)