# Find graph adjacency list (for undirected graph)
nodes=int(input("How many nodes: "))
edges=int(input("How many edges:"))
adjList={}
for i in range(edges):
    x,y=input("Enter %d edge:"%i).split()

    if x not in adjList:
        adjList[x]=[y]
    else:
        adjList[x].append(y)
    if y not in adjList:
        adjList[y]=[x]
    else:
        adjList[y].append(x)
print(adjList)