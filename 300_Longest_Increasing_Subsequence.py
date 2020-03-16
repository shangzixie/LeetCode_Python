class Solution1:
    """
    知道是对的，但是不知道为什么这样是对的
    """
    def lengthOfLIS(self, nums):
        size = len(nums)
        if size < 2:
            return size

        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue

            l, r = 0, len(cell) - 1
            while l < r:
                mid = l + (r - l) // 2
                if cell[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num
        return len(cell)


if __name__ == '__main__':

    a = Solution1()
    nums = [3,2,1,4,7,8,6,8,9]
    result = a.lengthOfLIS(nums)
