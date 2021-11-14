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