#네트워크 딜레이 타임

'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''

#풀이 방법

'''
다익스트라 알고리즘
'''

# # # # # # # # # # # # # # # # # # # # #

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        #그래프 인접 리스트 구성
        for u,v,w in times:
            graph[u].append((v,w))

        #큐 변수 : [(소요시간, 정점)]
        Q = [(0,K)]

        dist = collections.defaultdict(int)

        #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w;
                    heapq.heappush(Q,(alt,v))

        if len(dist) == N:
            return max(dist.values())

        return -1


# # # # # # # # # # # # # # # # # # # # #
