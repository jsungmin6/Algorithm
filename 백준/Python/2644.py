#문제이름 : 촌수계산

#풀이계획

#BFS
#인접 리스트로 연결
#출발점과 도착점 설정
#queue에 need_visit
#visited에 지나간 곳 체크
#queue가 갱신될 때마다 count

###############################################################

from collections import deque

n=int(input())
graph=[[] for i in range(n+1)]

start,end=map(int,input().split())

m=int(input())

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


visited=[False for i in range(n+1)]

def dfs(start):
    need_visit=deque([start])
    count=0
    while need_visit:
        qsize=len(need_visit)
        for i in range(qsize):
            node = need_visit.popleft()

            if node == end:
                return count

            visited[node]=True
            for j in graph[node]:
                if visited[j]==False:
                    need_visit.append(j)
        count+=1
    return -1

print(dfs(start))

#다른사람 풀이1


people = [[0]*11 for i in range(11)]
v = [0]*11

n = int(input(""))
p1, p2 = input("").split(" ")
m = int(input(""))

for i in range(m):
  x, y = input("").split(" ")
  x = int(x)
  y = int(y)
  people[x][y] = people[y][x] = 1

q = []
q.append(int(p1))

while q!=[] :
  present = q.pop(0)
  for i in range(1,n+1):
    if people[present][i] != 0 and v[i] == 0:
      v[i] = v[present]+1
      print(i)
      print(v)
      q.append(i)


if(v[int(p2)]!=0):
  print(v[int(p2)])
else:
  print(-1)
