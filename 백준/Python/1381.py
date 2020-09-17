N=4
M=5
V=1
data=[[1,2],[1,3],[1,4],[2,4],[3,4]]

def dfs(graph,start):
    visited,needvisit=list(),list()
    needvisit.append(start)

    while needvistit:
        node = needvisit.pop()
        if node not in visited:
            visited.append(node)
