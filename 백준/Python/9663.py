def dfs(array,start):
    visited,need_visit=list(),list()
    need_visit.append(start)

    while need_visit:
        node=need_visit.pop()
        if node not in visited:
            visited.append(node)
            inputData=array[node]
            inputData.sort(reverse=True)
            need_visit.extend(inputData)

    return visited

def bfs(array,start):
    visited,need_visit=list(),list()
    need_visit.append(start)

    while need_visit:
        node=need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            inputData=array[node]
            inputData.sort()
            need_visit.extend(inputData)

    return visited


N=5
M=5
V=3
data=[[5,4],[5,2],[1,2],[3,4],[3,1]]

array=[[] for i in range(N+1)]

for a,b in data:
    array[a].append(b)
    array[b].append(a)

bfs(array,V)

for i in dfs(array,V):
    print(i,end=' ')
print()
for i in bfs(array,V):
    print(i,end=' ')
