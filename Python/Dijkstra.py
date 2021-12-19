from math import inf
from queue import PriorityQueue
class Node:
    def __init__(self,node):
        self.name=node
        self.key=inf
        self.parent=None
        self.adj=[]    #[[b,4],[h,8]]
        self.visited=False
    def __lt__(self,other):
        return self.key<other.key

def dijkstra(source,nodes):
    q=PriorityQueue()
    nodes[source].key=0
    q.put(nodes[source])

    while not q.empty():
        u=q.get()
        u.visited=True

        for element in u.adj:
            v,w=element[0],element[1]
            if nodes[v].visited is False and nodes[v].key>(u.key+w):
                nodes[v].key=u.key+w
                nodes[v].parent=u.name
                q.put(nodes[v])
def main():
    n=int(input("How many nodes? "))
    nodes_name=input("Enter nodes name: ").split()
    nodes={}
    for element in nodes_name:
        nodes[element]=Node(element)
    e=int(input("How many edge ? "))
    for i in  range(e):
        u,v,w=input("Edge %d with weight: "%(i+1)).split()
        nodes[u].adj.append([v,int(w)])
    s=input("Enter source vertex: ")
    dijkstra(s,nodes)

    for element in nodes_name:
        print(nodes[element].name)
        print(nodes[element].key)
        print(nodes[element].parent)

if __name__=="__main__":
    main()
