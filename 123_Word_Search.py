DIRECTION = [(0, -1), (0, 1), (1, 0), (-1, 0)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                if self.dfs(board, word, "", visited, i, j):
                    return True

        return False

    def dfs(self, board, word, path, visited, i, j):
        if path and word[len(path) -1] != path[-1]:
            return False
        if len(word) == len(path) and word == path:
            return True

        path = path + board[i][j]
        visited.add((i, j))

        for dx, dy in DIRECTION:
            newx, newy = i + dx, j + dy
            if newx < 0 or newx >= len(board) or newy < 0 or newy >= len(board[0]) or (newx, newy) in visited:
                continue
            if self.dfs(board, word, path, visited, newx, newy):
                return True
        visited.remove((i,j))  #大bug ！！！ 绝对不能忘了回溯啊
        return True if len(word) == len(path) and word == path else False  #处理单个字符的情况



if __name__ == '__main__':
    board = ["ABCE","SFES","ADEE"]
    word = "ABCESEEEFS"
    a = Solution()
    print(a.exist(board, word))