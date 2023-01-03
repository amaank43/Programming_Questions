'''
https://devsnest.in/algo-challenges/redundant-connection?tab=question
'''
def solve(edges):
    # CODE HERE
        parent = [i for i in range(len(edges)+1)]
        def find(p):
            while p != parent[p]:
                p = parent[parent[p]]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            parent[p2] = p1
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
