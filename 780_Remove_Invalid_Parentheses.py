class Solution1:
    """
    @param s: The input string
    @return: Return all possible results
    版本1：未考虑回溯问题，只沿着一个路径走到底就结束了
    """

    def removeInvalidParentheses(self, s):
        self.results = []
        self.dfs(s, "", [])

        return self.results

    def dfs(self, s, path, stack):
        if not s and not stack:
            self.results.append(path)
            self.results
            return

        if s[0] == "(":
            stack.append(s[0])
            path +=  s[0]
            self.dfs(s[1:], path, stack)
        elif s[0] == ")" and not stack:
            self.dfs(s[1:], path, stack)
        elif s[0] == ")" and stack:
            stack.pop()
            path +=  s[0]
            self.dfs(s[1:], path, stack)

    """
    应该怎么设计回溯呢？？
    既保证了当前的这个字符选择或不选择，又保证当前字符前面的字符不会再被用到
    """
####################################################################
class Solution2:
    """
    @param s: The input string
    @return: Return all possible results

    版本2：加入for循环，解决问题， 并加入pop功能回溯
    """

    def removeInvalidParentheses(self, s):
        self.results = []
        self.dfs(s, "", [])
        print(self.results)
        return self.results

    def dfs(self, s, path, stack):
        if not s and not stack:
            self.results.append(path)
            return

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                path +=  s[i]
                self.dfs(s[i+1:], path, stack)
                if stack:
                    stack.pop()
                path = path[:-1]
            if s[i] == ")" and not stack:
                self.dfs(s[i+1:], path, stack)
            if s[i] == ")" and stack:
                stack.pop()
                path +=  s[i]
                self.dfs(s[i+1:], path, stack)
                path = path[:-1]
    """
    1. 为什么stack不是当前层的stack,从下一层回溯回来后，stack变成了递归后的stack？？
    2. 怎么去重？
    3. 怎么才能得到最佳结果，既delete minimum character
    """
####################################################################
class Solution3:
    """
    @param s: The input string
    @return: Return all possible results
    版本三：
    1. stack代表的地址永远是那一个地址，所以某i+1层stack改变了，回溯到i层，就是变后的stack;解决方法就是把stack写到def里面，用+，而不是用append。“+”意味着开了
    一个新的内存
    2. 不用s[i+1:]去进行下次递归，而用完整的s，加入startIndex来防止当前字符前面的字符被访问。然后，利用s[i] == s[i-1]: continue来去重
    3. 用下面的if判断来取得最优解
    """

    def removeInvalidParentheses(self, s):
        self.results = []
        self.dfs(s, 0, "", [])

        return self.results

    def dfs(self, s, startIndex, path, stack):
        if not stack and startIndex == len(s):
            if not self.results:
                self.results.append(path)
            elif len(path) > len(self.results[0]):
                self.results = []
                self.results.append(path)
            elif len(path) == len(self.results[0]):
                self.results.append(path)
            return

        for i in range(startIndex, len(s)):
            if s[i] == s[i - 1] and i >= startIndex and not stack:
                continue
            if s[i] == "(":
                self.dfs(s, i + 1, path + s[i], stack + [s[i]])
            if s[i] == ")" and not stack:
                self.dfs(s, i + 1, path, stack)
            if s[i] == ")" and stack:
                self.dfs(s, i + 1, path + s[i], stack[:-1])

"""
会出现重复答案，去重并不彻底，怎么去重？根本无法解决？
"""



####################################################################
class Solution:
    """
    @param s: The input string
    @return: Return all possible results

    最终版本：
    用left和right代替stack
    因为left和right一开始传入进去的初始值至最后left和right都为0，决定了传进去result的结果就是最优结果.

    1. 为什么startIndex是从i开始的，而不是i+1:因为有非“（）”的特殊符号: 例如输入"*)"
    2. left,right为多余的左右括号数量，所以当遇到左右括号时候，把多余的左右括号都删去，继续递归
    """

    def removeInvalidParentheses(self, s):
        res = []
        left, right = self.LeftRightCount(s)
        self.dfs(s, left, right, 0, res)
        if not res:
            res = [""]
        return res

    def dfs(self, s, left, right, start, res):
        if left == 0 and right == 0:
            if self.isvalid(s):
                res.append(s)
            return

        for i in range(start, len(s)):
            if i >= start and s[i] == s[i - 1]:
                continue
            if left > 0 and s[i] == '(':
                self.dfs(s[:i] + s[i + 1:], left - 1, right, i, res)
            if right > 0 and s[i] == ')':
                self.dfs(s[:i] + s[i + 1:], left, right - 1, i, res)

    def isvalid(self, s):
        left, right = self.LeftRightCount(s)
        return left == 0 and right == 0

    def LeftRightCount(self, s):
        """
        :param s:
        :return:
        返回的left和right为未配对的（配对后剩下的）左右括号的个数
        """
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right






if __name__ == '__main__':
    s = ")(f"
    a = Solution()
    a.removeInvalidParentheses(s)

