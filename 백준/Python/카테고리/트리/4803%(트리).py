import sys
input = sys.stdin.readline

def edge_num(i,graph):
    visited[i] = 1
    cnt=len(graph[i])

    for j in graph[i]:
        if visited[j] == 0:
            cnt += edge_num(j,graph)
    return cnt

def node_num(i,graph):
    passed[i] = 1
    cnt=1

    for j in graph[i]:
        if passed[j] == 0:
            cnt += node_num(j,graph)
    return cnt


case_num=0
while True:
    case_num+=1
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
        
    graph=[[] for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(1+n)
    passed=[0]*(1+n)
    tree_num=0
    for i in range(1,n+1):
        if visited[i] == 0:
            V=node_num(i,graph);
            E=edge_num(i,graph);
            if V-1 == E//2:
                tree_num+=1
    
    if tree_num == 0:
        print("Case {0}: No trees.".format(case_num))
    elif tree_num == 1:
        print("Case {0}: There is one tree.".format(case_num))
    else:
        print("Case {0}: A forest of {1} trees.".format(case_num,tree_num))

    
