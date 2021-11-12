from queue import Queue
edges = []
f = open('test.txt','r')
for i in f.readlines():
    tmp = i.split(",")
    edges.append((int(tmp[0]), int(tmp[1])))
nodes = []
for i in range(len(edges)):
    for j in edges[i]:
        if j not in nodes:
            nodes.append(j)
print("Input for directed graph = ",edges)
def adjacent_listd(nodes,edges):
    adj = {node:[] for node in nodes}
    for edge in edges:
        node1,node2 = edge[0],edge[1]
        adj[node1].append(node2)
    return adj
def adjacent_listud(nodes,edges):
    adj = {node:[] for node in nodes}
    for edge in edges:
        node1,node2 = edge[0],edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    return adj
adj_list = adjacent_listd(nodes,edges)
print('adjacency List',adj_list)
def adjacent_matrixd(nodes,edges):
    adj = [[0 for node in nodes]for node in nodes]
    for edge in edges:
        node1,node2 = edge[0],edge[1]
        adj[node1][node2] +=1
    return adj
adj_m=adjacent_matrixd(nodes,edges)
print('Adjacent matrix=',adj_m)
def adjacent_matrixud(nodes,edges):
    adj = [[0 for node in nodes]for node in nodes]
    for edge in edges:
        node1,node2 = edge[0],edge[1]
        adj[node1][node2] +=1
        adj[node2][node1] +=1
    return adj
def bfs(li,s_node):
    visited_node = {}
    parents = {}
    bfs_out = []
    queue = Queue()
    for node in li.keys():
        visited_node[node] = False
        parents [node] = None
    visited_node[s_node] = True
    queue.put(s_node)
    while not queue.empty():
        u = queue.get()
        bfs_out.append(u)
        for v in li[u]:
            if not visited_node[v]:
                visited_node[v] = True
                parents[v] = u
                queue.put(v)
    return bfs_out,parents
s = int(input("please Enter the starting node = "))
trav_path = bfs(adj_list,s)[0]
print(trav_path)
def short_path(p,de):
    path = []
    while de is not None:
        path.append(de)
        de = p[de]
    return path
source = int(input("please enter a source node = "))
destination = int(input("please enter a destination node = "))
parents = bfs(adj_list,source)[1]
s_path = short_path(parents,destination)
distance = len(s_path)
print('distance',distance)
s_path.reverse()
print('Shortest path',s_path)
output = open('output.txt','w')
d = 'adjacency list ='+str(adj_list)+'\ntraversal path ='+str(trav_path)+'\nshotest path ='+str(s_path)+'\nAdjacent matrix = '+str(adj_m)
output.write(d)