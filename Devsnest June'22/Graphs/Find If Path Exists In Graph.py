'''
https://devsnest.in/algo-challenges/find-if-path-exists-in-graph?tab=question

'''
def solve(n, edges, source, destination):
    # CODE HERE
        if source == destination:
            return 1
        graph = dict();
        
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        visited = [0]*n
        dq = deque([source])
        
        while dq:
            node = dq.popleft()
            
            for nbr in graph[node]:
                if nbr == destination:
                    return 1
                elif not visited[nbr]:
                    visited[nbr] = 1
                    dq.append(nbr)
        return 0
