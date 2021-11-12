inputData = open('inputdfs.txt','r').readlines()

n = int(inputData[0])
graph = {}
for i in range(n):
    graph[i] = []

for lines in inputData[1:]:
    a, b = lines.split()
    a, b = int(a), int(b)
    graph[a].append(b)
    if a == 0 and b == 0:
        break

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    visited = set()
    print("Following is the Depth-First Search")
    dfs(visited, graph, 0)
    print('\n', graph)