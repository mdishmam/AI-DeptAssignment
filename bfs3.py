def travarsePrint(graph):
    for it in graph:
        print(it, end=': ')
        for subit in graph[it]:
            print(subit, end=', ')
        print('\n', end='')

def BFS(visited, graph, node): #function for BFS
    queue =[]
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        #print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

def BFS_SP(graph, start, goal):

    visited = []
    queue = [[start]]
    if start == goal:
        print("\nFrom "+str(start)+" to "+str(goal)+" distance: 0")
        print("From "+str(start)+" to "+str(goal)+" path: "+str(start))
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    print("\nFrom "+str(start)+" to "+str(goal)+" path:", *new_path)
                    print("From "+str(start)+" to "+str(goal)+" Distance:", len(new_path)-1)
                    return
            visited.append(node)

    print("So sorry, but a connect in gpath doesn't exist :("+str(start)+" to "+str(goal)+")")
    return

def CreateGraphFromFile(fileName):
    inputData = open(fileName,'r').readlines()

    n = int(inputData[0])
    graph = {}
    count = 0

    for lines in inputData[1:]:
        a, b = lines.split()
        if a == '0' and b == '0':
            break
        try:
            graph[a].append(b)
        except:
            graph[a] = [b]
        try:
            graph[b].append(a)
        except:
            graph[b] = [a]
        count += 1

    connections = inputData[count+2:]
    return  graph, connections

if __name__ == '__main__':
    graph, connections = CreateGraphFromFile(fileName='input.txt')

    print('Following graph is given:')
    travarsePrint(graph)

    print('\nBFS of the following graph:')
    bfsNodes = BFS([], graph, 'a')
    print(bfsNodes)

    for path in connections:
        source, destination = path.split()
        BFS_SP(graph, source, destination)


