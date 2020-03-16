from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dictionary):

        self.wordSet = set()  # record all vertex and node
        self.nextVertex = {}  # current vertex to [all next vertex]
        self.level = {}  # record vertexs's level

        # add all vertex into wordSet
        self.wordSet.add(start)
        for word in dictionary:
            self.wordSet.add(word)

        # build relationship
        for word in self.wordSet:
            self.nextVertex[word] = []
            self.addItsNext(word)

        # get shorest length of path
        self.wordSet.clear()
        shorestLongth = self.bfs(start, end)

        self.results = []
        self.wordSet.clear()
        self.dfs(shorestLongth, )

    def addItsNext(self, word):
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter == word[i]:
                    continue
                nextWord = word[:i] + letter + word[i + 1:]
                if nextWord in self.wordSet:
                    self.nextVertex[word].append(nextWord)

    def bfs(self, start, end):

        queue = deque([start])
        step = 0
        self.vertex[start] = 0
        # bfs basic format
        while queue:
            step += 1

            for _ in range(len(queue)):
                vertex = queue.pop()
                # why I can add visited here
                if end == vertex:
                    return step

                for nextVertex in self.nextVertex[vertex]:
                    if nextVertex in self.wordSet:
                        continue
                    queue.append(nextVertex)
                    self.wordSet.add(nextVertex)  # when visited will be added ??
                    self.level[nextVertex] = step

    def dfs(self, shorestLongth, path, end):
        if len(path) > shorestLongth:
            return
        if len(path) == shorestLongth:
            if path[0] == end:
                self.results.append(list(path))

        for vertex in self.nextVertex:
            allnextvertex = self.nextvertex[vertex]
            for nextvertex in allnextvertex:
                if nextvertex not in self.wordSet and self.level(nextvertex) and self.level(
                        nextvertex) + currDeep < shorestLongth:
                    path.append(nextvertex)
                    wordSet.add(nextvertex)
                    self.dfs(shorestLongth, path, end)
                    path.pop()
                    wordSet.remove(nextvertex)


class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        self.results = []
        self.dfs(n, [], 0)

        return self.results

    def dfs(self, n, path, startIndex):
        if n == 1:
            self.results.append(list(path))
            return

        for i in range(startIndex, n + 1):
            if n % i != 0:
                continue
            path.append(i)
            self.dfs(n / i, path, i)
            path.pop()



