"""
Definition of ParentTreeNode:
"""

class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None



class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum3(self, root, target):

        self.results = []
        self.dfs1(root, target)

        return self.results

    def dfs1(self, root, target):
        if not root:
            return

        self.dfs2(root, target, set(), [])
        self.dfs1(root.left)
        self.dfs1(root.right)

    def dfs2(self, root, target, visited, path):
        if not root:
            return
        if root in visited:
            return
            # if target < 0:
        #    return

        target -= root.val
        visited.add(root)
        path.append(root.val)

        if target == 0:
            self.results.append(list(path))

        self.dfs2(root.left, target, visited, path)
        self.dfs2(root.right, target, visited, path)
        self.dfs2(root.parent, target, visited, path)

        target += root.val
        visited.remove(root)
        path.pop()



if __name__ == '__main__':
    root = ParentTreeNode(4)
    root.left = ParentTreeNode(3)
    root.right = ParentTreeNode(7)
    t2 = root.left
    t3 = root.right
    t3.left = ParentTreeNode(5)
    t3.right = ParentTreeNode(6)

    A = t3.left
    B = t3.right
    soluiton = Solution()
    soluiton.binaryTreePathSum3(root, 6)
