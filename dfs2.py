def CreateGraphFromFile(fileName):
    inputData = open(fileName,'r').readlines()

    n = int(inputData[0])
    graph = {}

    for lines in inputData[1:]:
        a, b = lines.split()
        if a == '0' and b == '0':
            break
        try:
            graph[a].append(b)
        except:
            graph[a] = [b]
        # try:
        #     graph[b].append(a)
        # except:
        #     graph[b] = [a]

    return  graph

def DFS(visited, graph, node):
    if node not in visited:
        print (node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)
            return visited

if __name__ == '__main__':
    graph = CreateGraphFromFile('inputdfs.txt')

    dfs_output = DFS(set(), graph, '0')

