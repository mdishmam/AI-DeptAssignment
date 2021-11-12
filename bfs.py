# graph = {
#     '5' : ['3','7'],
#     '3' : ['2', '4'],
#     '7' : ['8'],
#     '2' : [],
#     '4' : ['8'],
#     '8' : []
# }
inputData = open('input.txt','r').readlines()

n = int(inputData[0])
graph = {}
for i in range(n+1):
    graph[i] = []

count = 0
for lines in inputData[1:]:
    # print(lines)
    a, b = lines.split()
    a, b = int(a), int(b)
    graph[a].append(b)
    graph[b].append(a)
    count += 1
    if a == 0 and b == 0:
        break
connections = inputData[count+1:]


visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        #print(visited)

def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("\nFrom "+str(start)+" to "+str(goal)+" path: 0")
        print("From "+str(start)+" to "+str(goal)+" Distance: "+str(start))
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    print("\nFrom "+str(start)+" to "+str(goal)+" path:", *new_path)
                    print("From "+str(start)+" to "+str(goal)+" Distance:", len(new_path)-1)
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return


# Driver Code
print("Following is the Breadth-First Search")
# print(graph)
for it in graph:
    print(it, end=': ')
    for subit in graph[it]:
        print(subit, end=', ')
    print('\n')
for connection in connections:
    a, b = connection.split()
    a, b = int(a),int(b)
    if a == 0 and b == 0:
        break
    BFS_SP(graph, a, b)
