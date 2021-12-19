<<<<<<< HEAD
def dfs(node):
    DFS.append(node)
    color[node] = 'gray'

    for element in adj[node]:
        if color[element]=='white':
            dfs(element)
    color[node] = 'black'

nodes = input("Enter nodes name:").split(" ")
edges = int(input("Enter number of nodes: "))

adj = {}
color = {}
DFS = []
for node in nodes:
    adj[node] = []
    color[node] = 'white'

for edge in range(edges):
    x,y = input("Enter %d edge:"%(edge+1)).split(" ")
    adj[x].append(y)
    #if graph is directed then comment out next line 
    adj[y].append(x)

for node in nodes:
    if color[node]=='white':
        dfs(node)

print("Adjacency list \n", adj)
print("Graph color after visit\n", color)
=======
def dfs(node):
    DFS.append(node)
    color[node] = 'gray'

    for element in adj[node]:
        if color[element]=='white':
            dfs(element)
    color[node] = 'black'

nodes = input("Enter nodes name:").split(" ")
edges = int(input("Enter number of nodes: "))

adj = {}
color = {}
DFS = []
for node in nodes:
    adj[node] = []
    color[node] = 'white'

for edge in range(edges):
    x,y = input("Enter %d edge:"%(edge+1)).split(" ")
    adj[x].append(y)
    #if graph is directed then comment out next line 
    adj[y].append(x)

for node in nodes:
    if color[node]=='white':
        dfs(node)

print("Adjacency list \n", adj)
print("Graph color after visit\n", color)
>>>>>>> 54a9d921fb7297289da1d50a4a430fbefcea0ba1
print("DFS\n",DFS)