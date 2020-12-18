'''
0으로 갈수있는 경우는 인접한 수가 가는 최대 4개이다. 그 배열의 모양을 기억하고 조건처리해준후 bfs q에 넣어준다.
모양은 str로 변환해서 기억해야 할 것 같다.
'''
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(Map,empty):
    visited = {Map:1}
    q=deque([[Map,empty]])
    count=0
    while q:
        for _ in range(len(q)):
            m,e = q.popleft()

            if m == '123456780':
                return count

            for i in range(4):
                x,y = e//3 , e%3
                new_x = x+dx[i]
                new_y = y+dy[i]

                if new_x<0 or new_y <0 or new_x==3 or new_y==3:
                    continue
                
                new_e = new_x*3 + new_y

                #위치 교환
                m_list = list(m)
                m_list[e],m_list[new_e] = m_list[new_e],m_list[e]

                new_m = ''.join(m_list)

                if visited.get(new_m):
                    continue
                
                visited[new_m] = 1
                q.append([new_m,new_e])
        count+=1
    return -1


Map=""
for _ in range(3):
    Map+=input().replace(' ','')

empty = Map.index('0')

print(bfs(Map,empty))

