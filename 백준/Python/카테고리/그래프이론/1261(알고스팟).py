'''
풀이
다익스트라를 이용해 최단거리, 즉 최소 벽의 개수를 구한다.
벽이 있는 경로를 가중치 1, 없으면 0 으로 한다.
'''
import heapq
INF = 987654321

M,N = map(int,input().split())
mat = [list(map(int,list(input()))) for i in range(N)]
dist = [[INF for i in range(M) ] for j in range(N)]
dist[0][0] = 0
start = [0,0]
end = [N-1,M-1]
Q = [[0,0,0]] # 가중치 , x좌표, y좌표
dx=[0,0,1,-1]
dy=[1,-1,0,0]

while Q:
    w,x,y = heapq.heappop(Q)
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]

        if new_y < 0 or new_x <0 or new_x == N or new_y == M:
            continue
        if dist[new_x][new_y] !=INF:
            continue
        
        if mat[new_x][new_y] == 1:
            dist[new_x][new_y] = w+1
            heapq.heappush(Q,[w+1,new_x,new_y])
        else:
            dist[new_x][new_y] = w
            heapq.heappush(Q,[w,new_x,new_y])

print(dist[N-1][M-1])


