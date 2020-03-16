class Solution1:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def get_indegrees(self, graph):
        indegrees = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees

    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)

        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        topo_order = []
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None

            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == len(graph):
            return topo_order

        return None


class Solution2:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        if not org:
            return True
        if not seqs or not any(seqs):
            return False

        indegree_org = [1] * len(org)
        indegree_org[org[-1] - 1] = 0
        indegree_seqs = [0] * len(org)
        for seq in seqs:
            for index in seq:
                if index not in range(1, len(org) + 1):
                    return False
                indegree_seqs[index - 1] += 1
            indegree_seqs[index - 1] -= 1
        for i in range(len(org)):
            if indegree_org[i] > indegree_seqs[i]:
                return False
        return True


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    这个方法是错的！！
    """

    def sequenceReconstruction(self, org, seqs):
        # open a dictionary to store the degree of org
        # the first ele's indegree is 0
        indegree_org = {org[0]: 0}
        for i in range(1,len(org)):
            indegree_org[org[i]] = 1

        # store the indegree of seqs:
        indegree_seqs = {}
        for seq in seqs:
            for i in range(len(seq)):
                if i == 0:
                    if seq[i] not in indegree_seqs:
                        indegree_seqs[seq[i]] = 0
                    else:
                        continue

                elif seq[i] not in indegree_seqs:
                    indegree_seqs[seq[i]] = 1
                else:
                    indegree_seqs[seq[i]] += 1

            # compare

        for num in indegree_seqs:
            if num not in indegree_org:
                return False
            if indegree_seqs[num] < indegree_org[num]:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    org = [1,2,3]
    seqs = [[1,2],[1,3]]
    solution.sequenceReconstruction(org, seqs)