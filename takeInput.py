inputData = open('inputdfs.txt','r').readlines()

n = int(inputData[0])
graph = {}
for i in range(n):
    graph[i] = []

count = 0
for lines in inputData[1:]:
    # print(lines)
    a, b = lines.split()
    a, b = int(a), int(b)
    if a == 0 and b == 0:
        break
    graph[a].append(b)
    graph[b].append(a)
    count += 1

connections = inputData[count+1:]
for connection in connections:

