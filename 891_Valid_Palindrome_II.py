class Solution1:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    版本一：
    1. 用什么方法呢？
    2. 递归怎么样？ 怎么确定只删一次？
    """

    def validPalindrome(self, s):
        return self.dfs(s, 0 ,len(s)-1, 1)


    def dfs(self, s, left, right,count):
        if left >= right:
            return True

        if s[left] == s[right]:
            result1 = self.dfs(s, left+1, right-1, count)
        if s[left] != s[right] and count == 1:
            result2 = self.dfs(s, left, right-1, count-1) or self.dfs(s, left+1, right, count-1)


        return result1 or result2 or False
    """
    用count计只能删除几次；
    漏掉了result1和result2的初始值
    """
class Solution2:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    版本二：更新result1和2初始值为False
    """

    def validPalindrome(self, s):
        return self.dfs(s, 0 ,len(s)-1, 1)


    def dfs(self, s, left, right,count):
        if left >= right:
            return True

        result1, result2 = False, False
        if s[left] == s[right]:
            result1 = self.dfs(s, left+1, right-1, count)
        if s[left] != s[right] and count == 1:
            result2 = self.dfs(s, left, right-1, count-1) or self.dfs(s, left+1, right, count-1)


        return result1 or result2 or False
    """
    时间复杂度
    O（n） = n
    """
class Solution3:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    版本三：时间复杂度没什么改变，用两次双指针
    """

    def validPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -=1
        if left >= right:
            return True

        return self.isSubPalindrome(s, left+1, right) or self.isSubPalindrome(s, left, right-1)


    def isSubPalindrome(self,s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1

        return True


if __name__ == '__main__':
    solution = Solution1()
    s= "abca"
    solution.validPalindrome(s)
