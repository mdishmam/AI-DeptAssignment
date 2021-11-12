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

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 1)