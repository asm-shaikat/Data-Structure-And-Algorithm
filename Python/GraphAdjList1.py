# Find graph adjacency list (for directed graph)
nodes = int(input("How many nodes: "))
edges = int(input("How many edges: "))

adj = {}

for i in range(edges):
    x,y = input("Enter %d edges: "%i).split()
    
    if x not in adj:
        adj[x]=[y]
    else:
        adj[x].append(y)

print(adj)