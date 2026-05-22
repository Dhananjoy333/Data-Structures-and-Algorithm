n = 5 #nodes
m = 6 #edges
edges = [[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# Matrix Method
matrix = [[0 for _ in range(n+1)] for _ in range(n + 1)] 

for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

#List Method    
lst = [[] for _ in range(n+1)]

for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)
    
#Dictionary
my_dict = {}
for i in range(1,n+1):
    my_dict[i] = []

for u,v in edges:
    my_dict[u].append(v)
    my_dict[v].append(u)