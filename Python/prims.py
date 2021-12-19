from queue import PriorityQueue
from math import inf

class Node:
    def __init__(self, n):
        self.name = n
        self.key = inf
        self.parent = None
        self.adj = []
        self.inMST = False

    def __lt__(self, other):
        return self.key < other.key

node_name = input("Enter nodes' name: ").split()
e = int(input("How many edges: "))

nodes = dict()
for node in node_name:
    nodes[node] = Node(node)

print(nodes)
print("Enter edges' information (u v w).")
for i in range(e):
    u, v, w = input("Edge %d: " % (i+1)).split()
    nodes[u].adj.append([v, int(w)])
    nodes[v].adj.append([u, int(w)])

Q = PriorityQueue()
s = input("Enter source node: ")
nodes[s].key = 0
Q.put(nodes[s])

mstWeight = 0
print("Selected edges.")
while not Q.empty():
    u = Q.get()
    # print(u)

    if u.inMST is False:
        u.inMST = True
        mstWeight += u.key
        if u.parent is not None:
            print(u.parent, "-", u.name, " ", u.key)

        for element in u.adj:
            v = element[0]
            w = element[1]

            if nodes[v].inMST is False and nodes[v].key > w:
                nodes[v].key = w
                nodes[v].parent = u.name
                Q.put(nodes[v])

print("MST weight: %d" % mstWeight)
for node in list(nodes):
    print(nodes[node].key, nodes[node].parent, nodes[node].inMST, nodes[node].adj)
