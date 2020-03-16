import collections


"""
first thought:



self.minDepth: stores real depth of current node 

min_back_depth: from beginner node of an cycle, if some nodes are at the cycle path, all their min_back_depth will be the beginer node's depth  
or it will be n 

"""



class Solution:
    def criticalConnections(self, n, connections):
        self.Vertex_2_everyNode = collections.defaultdict(list)
        for u, v in connections:
            self.Vertex_2_everyNode[u].append(v)
            self.Vertex_2_everyNode[v].append(u)
        connections = set(map(tuple, (map(sorted, connections))))
        self.minDepth = [-1] * n



        self.dfs(0, 0, -1)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(connections)
    
    
    def dfs(self, node, depth, parent):
        if self.minDepth[node] >= 0: # this node has been visited
            return self.minDepth[node]

        self.minDepth[node] = depth   # current node : depth value
        min_back_depth = n
        for neighbor in self.Vertex_2_everyNode[node]:
            if neighbor == parent:
                continue
            prev_depth = self.dfs(neighbor, depth + 1, node)
            if prev_depth <= depth: # means there is a cycle
                connections.discard(tuple(sorted((node, neighbor))))

            min_back_depth = min(min_back_depth, prev_depth)

        return min_back_depth




if __name__ == '__main__':
    solution = Solution()
    n = 4
    connections =  [[0,1],[1,2],[2,0],[1,3]]
    solution.criticalConnections(n, connections)