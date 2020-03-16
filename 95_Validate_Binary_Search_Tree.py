"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    1. 用考虑一个结点只有左儿子或者右儿子其中一个的情况吗:
       用
    """

    def isValidBST(self, root):
        if not root or (not root.left and not root.right):
            return True

        result = self.dfs(root)
        return result

    def dfs(self, node):
        if not node:
            return True

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # 该节点左右儿子都不存在
        if not node.left and not node.right:
            return True
            # 该节点的subree不满足BST
        if not left or not right:
            return False

        # 该节点的subree满足BST,且左右儿子至少有一个在， 判断该节点
        if node.left and node.right:  # 如果左右儿子都存在
            if node.left.val < node.val < node.right.val:
                return True
            else:
                return False

        elif node.left and node.left.val < node.val:
            return True

        elif node.right and node.right.val > node.val:
            return True

        else:
            return False


"""
 左儿子的最大值 < 该结点的值 < 右儿子结点的最小值
"""


class Solution:
    """
    本题的难点就是从上到下就能确定左右子树的节点值的范围,
    判定子树的根是否存在于这个范围即可.
    """

    def isValidBST(self, root):
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, node, Min, Max):
        if not node:
            return True
        if node.val <= Min or node.val >= Max:
            return False

        left = self.dfs(node.left, Min, node.val)
        right = self.dfs(node.right, node.val, Max)

        if left and right:
            return True
        else:
            return False
