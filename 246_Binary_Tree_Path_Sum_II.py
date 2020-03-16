"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        self.results = []
        self.dfs1(root, target)
        return self.results

    def dfs1(self, root, target):
        if not root:
            return

        self.dfs2(root, target, [], set())
        self.dfs1(root.left, target)
        self.dfs1(root.right, target)

    def dfs2(self, root, target, path, visited):
        if not root:
            return
        if root in visited:
            return

        target -= root.val
        visited.add(root)
        path.append(root)

        if target == 0:
            self.results.append(list(path))

        self.dfs2(root.left, target, path, visited)
        self.dfs2(root.right, target, path, visited)

        target += root.val
        visited.pop(root)
        path.pop()