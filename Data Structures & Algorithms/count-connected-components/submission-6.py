class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # unionfind approach
        # find -> finding the parent node
        # union -> joining two trees together

        class UnionFind:
            def __init__(self, n):
                self.parent = {}
                self.rank = {}

                for i in range(n):
                    self.parent[i] = i
                    self.rank[i] = 0

            def find(self, n):
                p = n
                while p != self.parent[p]:
                    # memoization step
                    self.parent[p] = self.parent[self.parent[p]]
                    # go up a level
                    p = self.parent[p]
                
                return p

            def union(self, n1, n2) -> bool:
                """
                Try taking the union if different trees
                But if same tree just skip
                """
                p1 = self.find(n1)
                p2 = self.find(n2)

                # don't union they're actually the same tree
                # i.e. same root
                if p1 == p2:
                    return False

                if self.rank[p1] > self.rank[p2]:
                    self.parent[p2] = p1
                elif self.rank[p2] > self.rank[p1]:
                    self.parent[p1] = p2
                else:
                    self.parent[p1] = p2
                    self.rank[p2] += 1

                return True

        unionfind = UnionFind(n)
        for (node_a, node_b) in edges:
            unionfind.union(node_a, node_b)

        n_roots = 0
        for i in unionfind.parent:
            if unionfind.parent[i] == i:
                n_roots += 1
        return n_roots

        