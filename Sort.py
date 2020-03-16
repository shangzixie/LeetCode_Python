class Solution1:
    """
    quick sort
    """

    def sortIntegers2(self, A):
        self.quickSort(0, len(A) - 1, A)

    def quickSort(self, start, end, A):
        if start > end:
            return

        left, right = start, end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quickSort(start, right, A)
        self.quickSort(left, end, A)


class Solution:
    """
    merge sort
    """

    def sortIntegers2(self, A):
        temp = [0 for _ in range(len(A))]
        self.divided(A, 0, len(A) - 1, temp)


    def divided(self, A, start, end, temp):
        if start >= end:  #because in merge sort, start == end, there is no need for us to divided
            return

        mid = (start + end) // 2

        self.divided(A, start, mid, temp)
        self.divided(A, mid + 1, end, temp)
        self.merge(A, temp, start, end, mid)

    def merge(self, A, temp, start, end, mid):
        left = start
        right = mid + 1
        index = left

        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[index] = A[left]
                left += 1

            elif A[left] > A[right]:
                temp[index] = A[right]
                right += 1
            index += 1


        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1

        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
        for index in range(start, end+1):   # use start and end
            A[index] = temp[index]

if __name__ == '__main__':
    solution = Solution()
    A = [5,4,3,2,1]
    solution.sortIntegers2(A)