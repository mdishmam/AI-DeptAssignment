inputData = open('input.txt','r').readlines()

n = int(inputData[0])
graph = {}
# for i in range(n+1):
#     graph[i] = []

count = 0
for lines in inputData[1:]:
    a, b = lines.split()
    # a, b = int(a), int(b)
    # graph[a].append(b)
    # graph[b].append(a)
    if a == '0' and b == '0':
        break
    try:
        graph[a].append(b)
    except:
        graph[a] = [b]
    count += 1

