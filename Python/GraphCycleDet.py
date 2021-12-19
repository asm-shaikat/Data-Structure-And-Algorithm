<<<<<<< HEAD
def dfs(u):
    li.append(u)    
    color[u]='gray'

    for element in adj[u]:
        if color[element]=='gray':
            print("Cycle founded")
            exit()
        else:
            dfs(element)

    color[u]='black'

nodes=input("Enter nodes name:").split()
e=int(input("Enter number of edge:"))

isCycle=False
adj={}
color={}
li=[]
for element in nodes:
    adj[element]=[]
    color[element]='white'

for i in range(e):
    u,v=input("Edge %d:"%(i+1)).split()
    adj[u].append(v)
    # adj[v].append(u)
print("DFS:",end=" ")
for member in nodes:
    if color[member]=='white':
        dfs(member)
print()
print(adj)
print(color)
=======
def dfs(u):
    li.append(u)    
    color[u]='gray'

    for element in adj[u]:
        if color[element]=='gray':
            print("Cycle founded")
            exit()
        else:
            dfs(element)

    color[u]='black'

nodes=input("Enter nodes name:").split()
e=int(input("Enter number of edge:"))

isCycle=False
adj={}
color={}
li=[]
for element in nodes:
    adj[element]=[]
    color[element]='white'

for i in range(e):
    u,v=input("Edge %d:"%(i+1)).split()
    adj[u].append(v)
    # adj[v].append(u)
print("DFS:",end=" ")
for member in nodes:
    if color[member]=='white':
        dfs(member)
print()
print(adj)
print(color)
>>>>>>> 54a9d921fb7297289da1d50a4a430fbefcea0ba1
print(li)