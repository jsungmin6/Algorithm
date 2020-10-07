#코스 스케줄 ...어렵다

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

#풀이 방법

'''
순환구조를 찾으면 False 반환
탐색 종료 후 순환 노드 삭제
탐색 종료 후 방문 노드 추가
'''

# # # # # # # # # # # # # # # # # # # # # 책 풀이 재귀 활용

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        #그래프 구성
        for x,y in prerequisites:
            graph[x].append(y)

        traces = set()
        visited = set()

        def dfs(i):
            #순환 구조이면 False
            if i in traced:
                return False;
            #이미 방문했던 노드이면 False;
            if i in visited:
                return True;

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False;
            #탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            #탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True;

        #순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False;

        return True;

# # # # # # # # # # # # # # # # # # # # #
