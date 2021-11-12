inputData = open('input.txt','r').readlines()

n = int(inputData[0])
graph = {}
for i in range(n+1):
    graph[i] = []

count = 0
for lines in inputData[1:]:
    a, b = lines.split()
    a, b = int(a), int(b)
    graph[a].append(b)
    # graph[b].append(a)
    count += 1
    if a == 0 and b == 0:
        break
connections = inputData[count+1:]

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

if __name__ == '__main__':
    print(graph)
    # for it in graph:
    #     print(it, end=': ')
    #     for subit in graph[it]:
    #         print(subit, end=', ')
    #     print('\n')
    for connection in connections:
        a, b = connection.split()
        a, b = int(a),int(b)
        if a == 0 and b == 0:
            break
        BFS_SP(graph, a, b)
