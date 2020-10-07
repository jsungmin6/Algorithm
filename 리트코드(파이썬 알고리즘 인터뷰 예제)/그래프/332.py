#일정 재구성

'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

#풀이 방법

'''
stack or 재귀로 구현
그래프를 만들때 어휘순으로 만들고 첫번째 경로를 꺼내면서 그래프에서 제거를 해줘야 함.
갔던곳을 또 갈 수 있기에 pop로 아예 없애주어야 한다.
'''

# # # # # # # # # # # # # # # # # # # # # 책 풀이 재귀 활용

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        #그래프 순서대로 구성
        for a,b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            #첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        #다시 뒤집어 어휘 순 결과로
        return route[::-1]

# # # # # # # # # # # # # # # # # # # # # 책 풀이 stack 활용

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collectionsdefaultdict(list)
        #그래프 순서대로 구성
        for a,b in sorted(tickets):
            graph[a].append(b)

        route, stack = [],['JFK']
        while stack:
            #반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        #다시 뒤집어 어휘 순 결과로
        return route[::-1]
