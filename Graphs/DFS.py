def dfs(node,result,visited,adj):
    visited[node] = 1
    result.append(node)
    for n in adj[node]:
        if visited[n] == 0:
            dfs(n,result,visited,adj)
           
number_of_node = 9
adjacent_list = [
    [],
    [2, 4],
    [1, 3, 6],
    [2],
    [1, 5, 7],
    [4, 8],
    [2],
    [4, 8],
    [5, 7]
]
result = []
visited = [0] *(number_of_node+1)
dfs(1,result,visited,adjacent_list)
print(result)

