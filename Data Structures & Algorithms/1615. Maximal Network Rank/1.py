class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        # bidirectional road between ai and bi in roads[i] = [ai,bi]
        # network rank = number of directly connected roads to either city
        # depends on how many roads connected to two nodes?

        # simplified: Return the maximum number of roads connected between any two nodes

        # cities dont have to connected all together

        # randomly choose two nodes and see how many roads there are
        # N : number of nodes
        # M number of roads

        # O(N^2 * M)

        # find all the nodes
        # iterate through all pairs of nodes
        # check all roads to it
        # choosing an adjacent node just gets rid of one connection

        # keep track of the roads connecting to each node:
        # 0 : [1,3], 1 : [0,2,3], 2 : [1,3,4]
        # when we choose two pairs: if a node pair is contained in a connectedNode just subtract 1
        # then add the len(roads)

        # O(N^2)

        # take the max two values?

        neighbors = [set() for i in range(n)]
        degree = [0 for i in range(n)]

        for road in roads:
            val1, val2 = road[0], road[1]
            # add the neighbors
            neighbors[val1].add(val2)
            neighbors[val2].add(val1)
            degree[val1] += 1
            degree[val2] += 1

        # look through all pairs
        best = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if i in neighbors[j]:
                    rank -= 1
                best = max(best, rank)
        return best
