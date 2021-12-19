from queue import PriorityQueue
from math import inf


class Node:
    def __init__(self):
        self.key = inf
        self.parent = None


class Edge:
    def __init__(self, starting_node, end_node, weight):
        self.u = starting_node
        self.v = end_node
        self.w = weight


node_name = input("Enter nodes' name: ").split()
e = int(input("How many edges: "))

nodes = dict()
for node in node_name:
    nodes[node] = Node(node)

edges = list()
print("Enter edges' information (u v w).")
for i in range(e):
    u, v, w = input("Edge %d: " % (i+1)).split()
    edges.append(Edge(u, v, int(w)))

s = input("Enter source node: ")
nodes[s].key = 0
nodes[s].parent = s

for i in range(len(node_name)):
    for edge in edges:
        u, v, w = edge.u, edge.v, edge.w

        if nodes[v].key > nodes[u].key + w:
            nodes[v].key = nodes[u].key + w
            nodes[v].parent = u


def path_print(x):
    if nodes[x].parent is x:
        print(x, end=' ')

    if nodes[x].parent is not x:
        path_print(nodes[x].parent)
        print(x, end=' ')


d = input("Destination node: ")
print("Cost: %d" % nodes[d].key)
print("Path: ", end='')
path_print(d)

print()
for node in list(nodes):
    print(nodes[node].key, nodes[node].parent)
