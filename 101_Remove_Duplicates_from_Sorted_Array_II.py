class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        left = 0
        count = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                count = 1

            else:
                if count < 2:
                    left += 1
                    nums[left] = nums[right]
                    count += 1
        return left + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1,2,2,3,3,3]
    solution.removeDuplicates(nums)