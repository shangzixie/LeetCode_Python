class Solution1:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """

    """
    版本一：前缀积L[i] (不包括i）， 后缀积R[i]（不包括i )，再用L[i] * R[i]
    """

    def productExceptSelf(self, nums):
        # write your code here
        before = [1 for _ in range(len(nums))]
        after = [1 for _ in range(len(nums))]

        result = []

        for i in range(1, len(nums)):
            before[i] = before[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            after[j] = after[j + 1] * nums[j + 1]

        for i, j in zip(before, after):
            result.append(i * j)

        return result

    """
    时间复杂度n, 空间复杂度3n
    怎么优化空间复杂度？
    """


class Solution:

    """
    最终版本
    """

    def productExceptSelf(self, nums):

        products = [1] * len(nums)

        for i in range(1, len(nums)):
            products[i] = products[i-1] * nums[i-1]


        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= suffix
            suffix  *= nums[i]

        return products