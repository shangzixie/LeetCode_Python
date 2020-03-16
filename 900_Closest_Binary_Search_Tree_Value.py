"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:
    """
    brute force：
        traverse the whole tree, then transfer the tree to an array, use binary search to find it

    optimize:
        if current node is bigger than target, the next closest node is either the current node or left son
    """

    def closestValue(self, root, target):
        self.delt = float("inf")
        self.result = None
        self.dfs(root, target)

        return self.result

    def dfs(self, node, target):
        if not node:
            return
        if abs(node.val - target) > self.delt:
            return

        currDelt = abs(node.val - target)
        if currDelt <= self.delt:
            self.delt = currDelt
            self.result = node.val

        if node.val - target >= 0:
            self.dfs(node.left, target)
        else:
            self.dfs(node.right, target)

    """
    but this method cannot go though this case:
    {10,5,15,3,6,12,18,#,4,#,8}
    4.12
    
    
    """

class Solution:
    """
    the Final Version:
        change the second edge condition
    """

    def closestValue(self, root, target):
        self.delt = float("inf")
        self.result = None
        self.dfs(root, target)

        return self.result

    def dfs(self, node, target):
        if not node:
            return
        if target == node.val:
            self.result = node.val
            return

        currDelt = abs(node.val - target)
        if currDelt <= self.delt:
            self.delt = currDelt
            self.result = node.val

        if node.val - target >= 0:
            self.dfs(node.left, target)
        else:
            self.dfs(node.right, target)