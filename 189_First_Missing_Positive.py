class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        # 从index 0 到 n-1 检查可以swap的点，要swap的是1到n
        i = 0
        while i < len(A):
            # 要swap的值是【1，n】，
            # 该值对不应才swap：A[i]!= i+1
            # 该值要去的地方index是j = A[i]-1，所以保证swap两值不等才能swap，不然一直while 死循环
            while 0 < A[i] <= len(A) and A[i] != i + 1 and A[i] != A[A[i] - 1]:
                j = A[i] - 1
                A[i], A[j] = A[j], A[i]
            i += 1

            # 找到不对应的，就return， 没找到说明不缺，返回比最后一个大一的值
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        return len(A) + 1

if __name__ == '__main__':
    solution = Solution()
    A = [1,1]
    solution.firstMissingPositive(A)