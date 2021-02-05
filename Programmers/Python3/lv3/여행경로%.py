'''
그래프 만들고 정렬, dict를 사용하면 될 듯하다.
'''
from collections import defaultdict
from collections import deque
from copy import deepcopy

tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
def solution(tickets):
    graph = defaultdict(list)
    visited=[]
    for ticket in tickets:
        start,end = ticket
        graph[start].append(end)
    answer=[]
    q=deque([["ICN",["ICN"]]])
    while q:
        print("q:",q)
        p = q.popleft()
        print("p:",p)
        node = p[0]
        route = p[1]
        print("node:",node)
        print("route:",route)
        if len(route)-1 == len(tickets):
            return route
        graph[node].sort()
        for i in graph[node]:
            print("visited",visited)
            print("node+i : ",node+i)
            if (node+i) in visited: 
                continue
            visited.append(node+i)
            temp= deepcopy(route)
            temp.append(i)
            print('temp:',temp)
            q.append([i,temp])

    return answer

print(solution(tickets))


###DFS 재귀 풀이
from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 재귀 호출을 사용한 DFS
    def dfs(key, footprint):
        if len(footprint) == N + 1:
            return footprint

        for idx, country in enumerate(routes[key]):
            routes[key].pop(idx)

            fp = footprint[:] # deepcopy
            fp.append(country)

            ret = dfs(country, fp)
            if ret: return ret # 모든 티켓을 사용해 통과한 경우

            routes[key].insert(idx, country) # 통과 못했으면 티켓 반환

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])

    return answer

###스택풀이
from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 스택을 사용한 DFS
    def dfs():
        stack = ["ICN"]
        path = []  # 가려고하는 경로를 저장하는 변수
        while len(stack) > 0:  # stack이 비어있을 때까지
            top = stack[-1]
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    answer = dfs()
    return answer