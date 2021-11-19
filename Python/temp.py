n=int(input())
e=int(input())
adj={}
for i in range(e):
    x,y=input().split()
    if x not in adj:
        adj[x]=[y]
    else:
        adj[x].append(y)
    if y not in adj:
        adj[y]=[x]
    else:
        adj[y].append(x)
print(adj)
    